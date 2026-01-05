import pandas as pd
import numpy as np
from matplotlib.figure import Figure
import matplotlib as mpl
from .utils import timer

def _apply_style(fig: Figure):
    mpl.rcParams.update({
        "font.family": "DejaVu Sans Mono",
        "axes.titlesize": 12,
        "axes.labelsize": 10,
        "xtick.labelsize": 9,
        "ytick.labelsize": 9,
        "legend.fontsize": 9,
        "axes.linewidth": 1.0,
    })

    fig.subplots_adjust(left=0.08, right=0.92, top=0.88, bottom=0.16)
def _base_axes(ax, title: str, ylabel: str | None = None):
    ax.set_title(title, pad=8)
    if ylabel:
        ax.set_ylabel(ylabel)
    ax.grid(False)
    ax.tick_params(direction="in", length=4, width=1)

@timer
def plot_spending_by_category(fig: Figure, df: pd.DataFrame):
    fig.clear()
    _apply_style(fig)
    ax = fig.add_subplot(111)
    exp = df[df["type"] == "expense"].copy()
    if exp.empty:
        _base_axes(ax, "Spending by Category (no expense data)")
        ax.text(0.5, 0.5, "No data", ha="center", va="center")
        return
    grp = exp.groupby("category")["amount"].sum().sort_values(ascending=False)
    # Group small slices for readability
    if len(grp) > 8:
        top = grp.head(7)
        other = grp.iloc[7:].sum()
        grp = pd.concat([top, pd.Series({"Other": other})])
    # Pie plot
    wedges, *_ = ax.pie(
        grp.values,
        startangle=90,
        autopct="%1.0f%%"
    )
    ax.set_title("Spending by Category (Expenses)", pad=8)
    ax.axis("equal")
    # Adaptive legend (won't fly off screen)
    if ax.figure.get_size_inches()[0] < 9.0:
        ax.legend(wedges, [str(x) for x in grp.index], title="Category",
                  loc="upper right", frameon=True)
    else:
        ax.legend(wedges, [str(x) for x in grp.index], title="Category",
                  loc="center left", bbox_to_anchor=(0.96, 0.5),
                  frameon=True, borderaxespad=0.2)

@timer
def plot_income_vs_expense_by_month(fig: Figure, df: pd.DataFrame):
    fig.clear()
    _apply_style(fig)
    ax = fig.add_subplot(111)
    if df.empty:
        _base_axes(ax, "Income vs Expense by Month (no data)")
        ax.text(0.5, 0.5, "No data", ha="center", va="center")
        return
    d = df.copy()
    d["month"] = d["date"].str.slice(0, 7)
    inc = d[d["type"] == "income"].groupby("month")["amount"].sum()
    exp = d[d["type"] == "expense"].groupby("month")["amount"].sum()
    months = sorted(set(d["month"]))
    inc_vals = [float(inc.get(m, 0.0)) for m in months]
    exp_vals = [float(exp.get(m, 0.0)) for m in months]
    x = np.arange(len(months))
    width = 0.38
    ax.bar(x - width/2, inc_vals, width, label="Income")
    ax.bar(x + width/2, exp_vals, width, label="Expense")
    _base_axes(ax, "Income vs Expense by Month", ylabel="Amount")
    ax.set_xticks(x)
    ax.set_xticklabels(months, rotation=25, ha="right")
    # Adaptive legend (won't fly off screen)
    ax.legend(frameon=True, loc="upper left")

@timer
def plot_daily_expense_trend(fig: Figure, df: pd.DataFrame):
    fig.clear()
    _apply_style(fig)
    ax = fig.add_subplot(111)
    exp = df[df["type"] == "expense"].copy()
    if exp.empty:
        _base_axes(ax, "Daily Expense Trend (no expense data)")
        ax.text(0.5, 0.5, "No data", ha="center", va="center")
        return
    daily = exp.groupby("date")["amount"].sum().sort_index()
    y = daily.values
    x = np.arange(len(daily))
    # Line plot
    ax.plot(x, y, marker="o", markersize=3, linewidth=1.5)
    _base_axes(ax, "Daily Expense Trend", ylabel="Amount")
    # Fewer x labels to reduce clutter
    step = max(1, len(daily) // 10)
    ax.set_xticks(x[::step])
    ax.set_xticklabels(daily.index.astype(str)[::step], rotation=25, ha="right")

@timer
def plot_cumulative_balance(fig: Figure, df: pd.DataFrame):
    fig.clear()
    _apply_style(fig)
    ax = fig.add_subplot(111)
    if df.empty:
        _base_axes(ax, "Cumulative Balance (no data)")
        ax.text(0.5, 0.5, "No data", ha="center", va="center")
        return
    d = df.copy().sort_values("date", ascending=True)
    signed = np.where(d["type"] == "income", d["amount"], -d["amount"])
    d["signed"] = signed
    cum = d.groupby("date")["signed"].sum().cumsum()
    x = np.arange(len(cum))
    ax.plot(x, cum.values, linewidth=1.8)
    _base_axes(ax, "Cumulative Balance Over Time", ylabel="Balance")
    step = max(1, len(cum) // 10)
    ax.set_xticks(x[::step])
    ax.set_xticklabels(cum.index.astype(str)[::step], rotation=25, ha="right")
