import pandas as pd
from .utils import timer

@timer
def apply_filters(df: pd.DataFrame,
                  month: str = "",
                  tx_type: str = "",
                  category: str = "",
                  min_amt: str = "",
                  max_amt: str = "",
                  keyword: str = "") -> pd.DataFrame:
    out = df.copy()
    if out.empty:
        return out
    if month.strip():
        out = out[out["date"].str.startswith(month.strip())]
    if tx_type.strip().lower() in ["income", "expense"]:
        out = out[out["type"].str.lower() == tx_type.strip().lower()]
    if category.strip():
        out = out[out["category"] == category.strip()]
    if keyword.strip():
        k = keyword.strip().lower()
        out = out[out["note"].str.lower().str.contains(k, na=False)]
    try:
        if min_amt.strip():
            out = out[out["amount"] >= float(min_amt)]
    except ValueError:
        pass
    try:
        if max_amt.strip():
            out = out[out["amount"] <= float(max_amt)]
    except ValueError:
        pass
    return out.sort_values("date", ascending=False)

@timer
def summary_metrics(df: pd.DataFrame) -> dict:
    if df.empty:
        return {"income": 0.0, "expense": 0.0, "net": 0.0, "avg_per_day": 0.0}
    income = df.loc[df["type"] == "income", "amount"].sum()
    expense = df.loc[df["type"] == "expense", "amount"].sum()
    net = income - expense
    days = df["date"].nunique()
    avg_per_day = (expense / days) if days else 0.0
    return {
        "income": float(income),
        "expense": float(expense),
        "net": float(net),
        "avg_per_day": float(avg_per_day),
    }

@timer
def find_outliers_expenses_iqr(df: pd.DataFrame, k: float = 1.5) -> pd.DataFrame:
    # Quick IQR outlier detection:
    # - Find Q1 (25%) and Q3 (75%) of expense amounts.
    # - IQR = Q3 - Q1, it's a simple measure of spread that ignores extremes.
    # - Anything below Q1 - k*IQR or above Q3 + k*IQR is flagged as an outlier.
    # - k is the sensitivity (1.5 is the usual choice).
    # - If IQR == 0 (all values identical), there's nothing weird to flag, so
    #   we just return an empty result.
    if df.empty:
        return df
    exp = df[df["type"] == "expense"].copy()
    if exp.empty:
        return exp
    q1 = exp["amount"].quantile(0.25)
    q3 = exp["amount"].quantile(0.75)
    iqr = q3 - q1
    if iqr == 0:
        # all expenses same, no meaningful outliers
        return exp.iloc[0:0].copy()
    low = q1 - k * iqr
    high = q3 + k * iqr
    out = exp[(exp["amount"] < low) | (exp["amount"] > high)].copy()
    out["bound_low"] = low
    out["bound_high"] = high
    return out.sort_values("amount", ascending=False)
