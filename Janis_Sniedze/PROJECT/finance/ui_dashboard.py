from tkinter import ttk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from .utils import log_action
from .plots import (
    plot_spending_by_category,
    plot_income_vs_expense_by_month,
    plot_daily_expense_trend,
    plot_cumulative_balance,
)

class DashboardTab(ttk.Frame):
    def __init__(self, parent, app):
        super().__init__(parent)
        self.app = app
        self._build()

    def _build(self):
        outer = ttk.Frame(self, padding=12)
        outer.pack(fill="both", expand=True)
        btns = ttk.LabelFrame(outer, text="Charts (uses current filters from Transactions tab)", padding=10)
        btns.pack(fill="x")
        ttk.Button(btns, text="Spending by Category (Pie)", command=self.chart_spending).pack(side="left", padx=6)
        ttk.Button(btns, text="Income vs Expense by Month", command=self.chart_income_vs_expense).pack(side="left", padx=6)
        ttk.Button(btns, text="Daily Expense Trend", command=self.chart_daily).pack(side="left", padx=6)
        ttk.Button(btns, text="Cumulative Balance", command=self.chart_balance).pack(side="left", padx=6)
        self.fig = Figure(figsize=(9, 4.8), dpi=100)
        self.canvas = FigureCanvasTkAgg(self.fig, master=outer)
        self.canvas.get_tk_widget().pack(fill="both", expand=True, pady=10)
        self.chart_spending()

    def _draw(self, plot_fn):
        df_view = self.app.get_current_view_df()
        plot_fn(self.fig, df_view)
        self.canvas.draw()

    @log_action("CHART_SPENDING")
    def chart_spending(self):
        self._draw(plot_spending_by_category)

    @log_action("CHART_INCOME_VS_EXPENSE")
    def chart_income_vs_expense(self):
        self._draw(plot_income_vs_expense_by_month)

    @log_action("CHART_DAILY")
    def chart_daily(self):
        self._draw(plot_daily_expense_trend)

    @log_action("CHART_BALANCE")
    def chart_balance(self):
        self._draw(plot_cumulative_balance)
