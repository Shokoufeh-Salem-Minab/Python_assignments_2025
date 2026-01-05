import random
from datetime import datetime, timedelta
import pandas as pd
import tkinter as tk
from tkinter import ttk, messagebox
from .config import COLUMNS, DEFAULT_CATEGORIES
from .storage import load_df, save_df, generate_txn_id
from .utils import log_action

class AddEditTab(ttk.Frame):
    def __init__(self, parent, app):
        super().__init__(parent)
        self.app = app
        self.editing_id = None
        self._build()

    def _build(self):
        frm = ttk.Frame(self, padding=12)
        frm.pack(fill="both", expand=True)
        ttk.Label(frm, text="Date (YYYY-MM-DD):").grid(row=0, column=0, sticky="w")
        self.var_date = tk.StringVar(value=datetime.now().strftime("%Y-%m-%d"))
        ttk.Entry(frm, textvariable=self.var_date, width=20).grid(row=0, column=1, sticky="w", padx=8)
        ttk.Label(frm, text="Type:").grid(row=1, column=0, sticky="w")
        self.var_type = tk.StringVar(value="expense")
        ttk.Combobox(frm, textvariable=self.var_type, values=["expense", "income"], state="readonly", width=18)\
            .grid(row=1, column=1, sticky="w", padx=8)
        ttk.Label(frm, text="Category:").grid(row=2, column=0, sticky="w")
        self.var_category = tk.StringVar(value=DEFAULT_CATEGORIES[0])
        self.cmb_category = ttk.Combobox(frm, textvariable=self.var_category, values=DEFAULT_CATEGORIES,
                                         width=18, state="readonly")
        self.cmb_category.grid(row=2, column=1, sticky="w", padx=8)
        ttk.Label(frm, text="Amount:").grid(row=3, column=0, sticky="w")
        self.var_amount = tk.StringVar(value="")
        ttk.Entry(frm, textvariable=self.var_amount, width=20).grid(row=3, column=1, sticky="w", padx=8)
        ttk.Label(frm, text="Note:").grid(row=4, column=0, sticky="w")
        self.var_note = tk.StringVar(value="")
        ttk.Entry(frm, textvariable=self.var_note, width=60).grid(row=4, column=1, sticky="w", padx=8)
        btns = ttk.Frame(frm)
        btns.grid(row=6, column=0, columnspan=2, sticky="w", pady=12)
        ttk.Button(btns, text="Add Transaction", command=self.add_transaction).pack(side="left", padx=(0, 8))
        ttk.Button(btns, text="Update Transaction", command=self.update_transaction).pack(side="left", padx=(0, 8))
        ttk.Button(btns, text="Clear Form", command=self.clear_form).pack(side="left", padx=(0, 8))
        ttk.Button(btns, text="Generate Demo Data", command=self.generate_demo_data).pack(side="left")
        self.lbl_edit = ttk.Label(frm, text="Not editing (Add mode).")
        self.lbl_edit.grid(row=7, column=0, columnspan=2, sticky="w")
        for i in range(8):
            frm.grid_rowconfigure(i, pad=6)

    def set_categories(self, categories: list[str]):
        self.cmb_category["values"] = categories
        if self.var_category.get() not in categories:
            self.var_category.set(categories[0])

    def _validate(self):
        try:
            entered_dt = datetime.strptime(self.var_date.get().strip(), "%Y-%m-%d").date()
        except ValueError:
            messagebox.showerror("Invalid date", "Use YYYY-MM-DD (example: 2026-01-05).")
            return None
        today = datetime.now().date()
        if entered_dt > today:
            messagebox.showerror("Invalid date", "Date cannot be in the future.")
            return None
        tx_type = self.var_type.get().strip().lower()
        if tx_type not in ["income", "expense"]:
            messagebox.showerror("Invalid type", "Type must be income or expense.")
            return None
        cat = self.var_category.get().strip()
        if not cat:
            messagebox.showerror("Missing category", "Category cannot be empty.")
            return None
        try:
            amt = float(self.var_amount.get().strip())
            if amt <= 0:
                raise ValueError
        except ValueError:
            messagebox.showerror("Invalid amount", "Amount must be a number > 0.")
            return None
        return {
            "date": self.var_date.get().strip(),
            "type": tx_type,
            "category": cat,
            "amount": float(amt),
            "note": self.var_note.get().strip(),
        }

    def clear_form(self):
        self.editing_id = None
        self.var_date.set(datetime.now().strftime("%Y-%m-%d"))
        self.var_type.set("expense")
        self.var_amount.set("")
        self.var_note.set("")
        self.lbl_edit.config(text="Not editing (Add mode).")

    @log_action("ADD_TRANSACTION")
    def add_transaction(self):
        data = self._validate()
        if data is None:
            return
        df = load_df()
        existing = set(df["id"].astype(str)) if not df.empty else set()
        txid = generate_txn_id(existing)
        row = pd.DataFrame([{"id": txid, **data}], columns=COLUMNS)
        df2 = pd.concat([df, row], ignore_index=True)
        save_df(df2)
        self.clear_form()
        self.app.refresh_all()
        messagebox.showinfo("Added", f"Transaction added: {txid}")

    @log_action("UPDATE_TRANSACTION")
    def update_transaction(self):
        if not self.editing_id:
            messagebox.showwarning("Not editing", "Click 'Edit Selected' first in Transactions tab.")
            return
        data = self._validate()
        if data is None:
            return
        df = load_df()
        mask = df["id"].astype(str) == str(self.editing_id)
        if not mask.any():
            messagebox.showerror("Missing", "Could not find transaction to update.")
            self.clear_form()
            self.app.refresh_all()
            return
        for k, v in data.items():
            df.loc[mask, k] = v

        save_df(df)
        updated_id = self.editing_id
        self.clear_form()
        self.app.refresh_all()
        messagebox.showinfo("Updated", f"Transaction updated: {updated_id}")

    def load_for_edit(self, row_values: list):
        # Row_values in column order
        self.editing_id = row_values[0]
        self.var_date.set(row_values[1])
        self.var_type.set(row_values[2])
        self.var_category.set(row_values[3])
        self.var_amount.set(str(row_values[4]))
        self.var_note.set(row_values[5])
        self.lbl_edit.config(text=f"Editing: {self.editing_id}")

    @log_action("GENERATE_DEMO_DATA")
    def generate_demo_data(self):
        df = load_df()
        existing = set(df["id"].astype(str)) if not df.empty else set()
        categories = list(self.cmb_category["values"]) or DEFAULT_CATEGORIES
        today = datetime.now().date()

        rows = []
        for _ in range(30):
            txid = generate_txn_id(existing)
            existing.add(txid)
            d = today - timedelta(days=random.randint(0, 120))
            tx_type = random.choice(["expense", "income"])
            category = random.choice(categories)
            if tx_type == "income":
                amount = round(random.uniform(100, 900), 2)
                note = random.choice(["salary", "gift", "refund", "bonus"])
            else:
                # 10% chance of a large expense outlier
                if random.random() < 0.10:
                    amount = round(random.uniform(250, 800), 2)   # Outlier expense
                    note = random.choice(["rent", "electronics", "medical", "emergency"])
                else:
                    amount = round(random.uniform(3, 120), 2)
                    note = random.choice(["lunch", "bus", "groceries", "coffee", "subscription"])
            rows.append({
                "id": txid,
                "date": d.strftime("%Y-%m-%d"),
                "type": tx_type,
                "category": category,
                "amount": amount,
                "note": note
            })
        df2 = pd.concat([df, pd.DataFrame(rows, columns=COLUMNS)], ignore_index=True)
        save_df(df2)
        self.app.refresh_all()
        messagebox.showinfo("Demo Data", "Added 30 demo transactions.")
