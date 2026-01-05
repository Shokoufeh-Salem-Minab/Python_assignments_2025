from pathlib import Path  # provide filesystem path helpers used for data storage
from datetime import datetime  # provide current date when none is supplied
import pandas as pd  # use pandas for simple CSV-backed table operations

dataDir = Path(__file__).parent / "data"  # folder where CSV data is stored
dataFile = dataDir / "expenses.csv"  # specific CSV file path used by the module
columns = ["date", "category", "amount", "description"]  # expected CSV columns and their order


def ensureDataFile():  # ensure the storage folder and CSV file exist before reads/writes
    dataDir.mkdir(exist_ok=True)  # create the folder when missing. This avoids write errors later
    if not dataFile.exists():  # when no CSV exists create an empty one with proper headers
        df = pd.DataFrame(columns=columns)  # empty frame with expected columns
        df.to_csv(dataFile, index=False)  # write the empty CSV to disk so later reads succeed


def loadExpenses():  # read the CSV into a DataFrame, creating the file first if needed
    ensureDataFile()  # guarantee storage is present before attempting to read
    df = pd.read_csv(dataFile, parse_dates=["date"]) if dataFile.exists() else pd.DataFrame(columns=columns)  # read CSV with date parsing
    return df  # return the loaded DataFrame (possibly empty)


def saveExpenses(df: pd.DataFrame):  # persist the provided DataFrame to the CSV file
    dataDir.mkdir(exist_ok=True)  # ensure directory exists before writing. This is safe to call repeatedly
    df.to_csv(dataFile, index=False)  # write the CSV without adding an extra index column


def addExpense(category: str, amount: float, description: str, date: str | None = None) -> pd.DataFrame:  # append a new expense and return updated DataFrame
    if date is None:  # when date not given use today's date
        dateVal = datetime.now().date()  # get current local date
    else:
        dateVal = pd.to_datetime(date).date()  # parse supplied date string to a date object
    df = loadExpenses()  # load existing entries to append to them
    new = {"date": dateVal.isoformat(), "category": category, "amount": float(amount), "description": description}  # build new row as a dict
    df = pd.concat([df, pd.DataFrame([new])], ignore_index=True)  # append the new row preserving column order
    saveExpenses(df)  # persist changes back to disk immediately
    return df  # return the updated DataFrame so callers can inspect it


def summarizeByCategory() -> pd.DataFrame:  # aggregate total amounts per category and return a tidy DataFrame
    df = loadExpenses()  # load all recorded expenses first
    if df.empty:  # return an empty summary with expected columns when there are no entries
        return pd.DataFrame(columns=["category", "total"])  # empty summary structure
    df["amount"] = pd.to_numeric(df["amount"])  # ensure amount column is numeric for aggregation
    s = df.groupby("category", as_index=False)["amount"].sum().rename(columns={"amount": "total"}).sort_values("total", ascending=False)  # compute totals and sort
    return s  # return the aggregated summary


def latestEntries(n: int = 5) -> pd.DataFrame:  # return the most recent n expense rows
    df = loadExpenses()  # load stored expenses before slicing
    if df.empty:  # nothing to show when empty
        return df  # return the empty DataFrame to the caller
    if "date" in df.columns:  # when dates exist, parse and sort by date to get the latest
        df["date"] = pd.to_datetime(df["date"])  # convert any string dates to pandas timestamps
        return df.sort_values("date", ascending=False).head(n)  # return the top n most recent entries
    return df.tail(n)  # fallback: return the last n rows if no date column present


__all__ = [
    "ensureDataFile",
    "loadExpenses",
    "saveExpenses",
    "addExpense",
    "summarizeByCategory",
    "latestEntries",
]
