import os
import csv
import random
import pandas as pd
from .config import DATA_DIR, CSV_PATH, COLUMNS

def ensure_dirs():
    os.makedirs(DATA_DIR, exist_ok=True)

def ensure_csv_exists():
    ensure_dirs()
    if not os.path.exists(CSV_PATH):
        with open(CSV_PATH, "w", newline="", encoding="utf-8") as f:
            csv.writer(f).writerow(COLUMNS)

def load_df() -> pd.DataFrame:
    ensure_csv_exists()
    # empty file safe
    if os.path.getsize(CSV_PATH) == 0:
        return pd.DataFrame(columns=COLUMNS)
    try:
        df = pd.read_csv(CSV_PATH, dtype={"id": str})
    except pd.errors.EmptyDataError:
        return pd.DataFrame(columns=COLUMNS)
    if df.empty:
        return pd.DataFrame(columns=COLUMNS)
    # CSVs are messy. Force columns to sane types so other code doesn't freak out:
    # - amount: try to parse as number, bad/missing -> 0.0 (so math works)
    df["amount"] = pd.to_numeric(df["amount"], errors="coerce").fillna(0.0)
    # - date: keep as string (YYYY-MM-DD). Avoid pandas auto-timestamp shenanigans.
    df["date"] = df["date"].astype(str)
    # - type: normalize to lowercase so filters like 'income'/'expense' behave.
    df["type"] = df["type"].astype(str).str.lower()
    # - category: strip extra spaces so 'food' and ' food ' don't look different.
    df["category"] = df["category"].astype(str).str.strip()
    # - note: replace missing with a friendly default so UI doesn't show 'nan'.
    df["note"] = df["note"].fillna("Not Specified").astype(str)
    return df[COLUMNS]

def save_df(df: pd.DataFrame) -> None:
    ensure_csv_exists()
    df = df.copy()[COLUMNS]
    with open(CSV_PATH, "w", newline="", encoding="utf-8") as f:
        df.to_csv(f, index=False)

def generate_txn_id(existing_ids: set[str]) -> str:
    while True:
        txid = f"TXN-{random.randint(100000, 999999)}"
        if txid not in existing_ids:
            return txid
