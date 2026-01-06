import tkinter as tk
from tkinter import ttk, messagebox
from .config import COLUMNS
from .storage import load_df, save_df
from .analytics import apply_filters, summary_metrics, find_outliers_expenses_iqr
from .utils import log_action, compact_number

class TransactionsTab(ttk.Frame):
    def __init__(self, parent, app):
        super().__init__(parent)
        self.app = app
        self.df_all = load_df()
        self.df_view = self.df_all.copy()
        self._build()

    def _build(self):
        outer = ttk.Frame(self, padding=12)
        outer.pack(fill="both", expand=True)
        filters = ttk.LabelFrame(outer, text="Filters", padding=10)
        filters.pack(fill="x")
        self.var_month = tk.StringVar(value="")
        self.var_type = tk.StringVar(value="")
        self.var_cat = tk.StringVar(value="")
        self.var_min = tk.StringVar(value="")
        self.var_max = tk.StringVar(value="")
        self.var_kw = tk.StringVar(value="")
        ttk.Label(filters, text="Month (YYYY-MM):").grid(row=0, column=0, sticky="w")
        ttk.Entry(filters, textvariable=self.var_month, width=12).grid(row=0, column=1, sticky="w", padx=6)
        ttk.Label(filters, text="Type:").grid(row=0, column=2, sticky="w")
        ttk.Combobox(filters, textvariable=self.var_type, values=["", "expense", "income"], state="readonly", width=10)\
            .grid(row=0, column=3, sticky="w", padx=6)
        ttk.Label(filters, text="Category:").grid(row=0, column=4, sticky="w")
        self.cmb_cat = ttk.Combobox(filters, textvariable=self.var_cat, values=[""], width=18, state="readonly")
        self.cmb_cat.grid(row=0, column=5, sticky="w", padx=6)
        ttk.Label(filters, text="Min Amt:").grid(row=1, column=0, sticky="w")
        ttk.Entry(filters, textvariable=self.var_min, width=12).grid(row=1, column=1, sticky="w", padx=6)
        ttk.Label(filters, text="Max Amt:").grid(row=1, column=2, sticky="w")
        ttk.Entry(filters, textvariable=self.var_max, width=12).grid(row=1, column=3, sticky="w", padx=6)
        ttk.Label(filters, text="Keyword:").grid(row=1, column=4, sticky="w")
        ttk.Entry(filters, textvariable=self.var_kw, width=18).grid(row=1, column=5, sticky="w", padx=6)
        ttk.Button(filters, text="Apply", command=self.refresh_table).grid(row=0, column=6, rowspan=2, padx=10)
        ttk.Button(filters, text="Clear", command=self.clear_filters).grid(row=0, column=7, rowspan=2, padx=0)
        mid = ttk.Frame(outer)
        mid.pack(fill="both", expand=True, pady=10)
        self.tree = ttk.Treeview(mid, columns=COLUMNS, show="headings", height=18, selectmode="extended")
        for c in COLUMNS:
            self.tree.heading(c, text=c.title())
            if c == "note":
                self.tree.column(c, width=420, anchor="w")
            elif c == "amount":
                self.tree.column(c, width=110, anchor="e")  # right align numbers
            elif c == "date":
                self.tree.column(c, width=115, anchor="w")
            elif c == "type":
                self.tree.column(c, width=90, anchor="w")
            elif c == "category":
                self.tree.column(c, width=140, anchor="w")
            else:
                self.tree.column(c, width=140, anchor="w")
        self.tree.pack(side="left", fill="both", expand=True)
        yscroll = ttk.Scrollbar(mid, orient="vertical", command=self.tree.yview)
        self.tree.configure(yscrollcommand=yscroll.set)
        yscroll.pack(side="right", fill="y")
        bottom = ttk.Frame(outer)
        bottom.pack(fill="x")
        ttk.Button(bottom, text="Edit Selected", command=self.edit_selected).pack(side="left", padx=(0, 8))
        ttk.Button(bottom, text="Delete Selected", command=self.delete_selected).pack(side="left", padx=(0, 8))
        ttk.Button(bottom, text="Show Outliers", command=self.show_outliers_popup).pack(side="left")
        self.lbl_summary = ttk.Label(outer, text="")
        self.lbl_summary.pack(anchor="w", pady=(8, 0))

    def set_categories(self, categories: list[str]):
        self.cmb_cat["values"] = [""] + categories
        if self.var_cat.get() and self.var_cat.get() not in categories:
            self.var_cat.set("")

    def clear_filters(self):
        self.var_month.set("")
        self.var_type.set("")
        self.var_cat.set("")
        self.var_min.set("")
        self.var_max.set("")
        self.var_kw.set("")
        self.refresh_table()

    def get_filtered_view_df(self):
        return apply_filters(
            self.df_all,
            month=self.var_month.get(),
            tx_type=self.var_type.get(),
            category=self.var_cat.get(),
            min_amt=self.var_min.get(),
            max_amt=self.var_max.get(),
            keyword=self.var_kw.get(),
        )
        
    def _get_filtered_view_df_metrics_for_header(self) -> str:
        df_view = self.get_filtered_view_df()
        m = summary_metrics(df_view)
        return f"Income {compact_number(m['income'])} | Expense {compact_number(m['expense'])} | Net {compact_number(m['net'])}"

    def refresh_table(self):
        self.df_all = load_df()
        self.df_view = self.get_filtered_view_df()
        for item in self.tree.get_children():
            self.tree.delete(item)
        self.tree.tag_configure("odd", background="#fafafa")
        self.tree.tag_configure("even", background="#ffffff")
        for i, (_, row) in enumerate(self.df_view.iterrows()):
            stripe = "even" if i % 2 == 0 else "odd"
            kind = str(row.get("type", "")).lower()
            tint = "income" if kind == "income" else "expense"
            vals = []
            for c in COLUMNS:
                if c == "amount":
                    vals.append(f"{float(row[c]):.3f}")
                else:
                    vals.append(row[c])
            self.tree.insert("", "end", values=vals, tags=(stripe, tint))
        # Tell app to sync dashboard view if needed
        self.app.on_table_refreshed()

    @log_action("EDIT_SELECTED")
    def edit_selected(self):
        sel = self.tree.selection()
        if not sel:
            messagebox.showwarning("No selection", "Select a row first.")
            return
        if len(sel) > 1:
            messagebox.showwarning("Multiple selected", "You can only edit one transaction at a time.")
            return
        vals = list(self.tree.item(sel[0], "values"))
        self.app.start_edit(vals)

    @log_action("DELETE_SELECTED")
    def delete_selected(self):
        sel = self.tree.selection()
        if not sel:
            messagebox.showwarning("No selection", "Select one or more rows first.")
            return
        ids = []
        for item in sel:
            vals = self.tree.item(item, "values")
            ids.append(vals[0])
        if len(ids) == 1:
            msg = f"Delete {ids[0]}?"
        else:
            msg = f"Delete {len(ids)} transactions?"
        if not messagebox.askyesno("Confirm delete", msg):
            return
        df = load_df()
        df = df[~df["id"].astype(str).isin([str(i) for i in ids])]
        save_df(df)
        self.refresh_table()


    @log_action("SHOW_OUTLIERS")
    def show_outliers_popup(self):
        df_view = self.get_filtered_view_df()
        # To ensure we have the latest data
        self.df_all = load_df()
        df_view = self.get_filtered_view_df()
        out = find_outliers_expenses_iqr(df_view, k=1.5)
        win = tk.Toplevel(self)
        win.title("Outliers (Expenses) | IQR Method")
        win.geometry("860x420")
        cols = ["id", "date", "category", "amount", "note"]
        tree = ttk.Treeview(win, columns=cols, show="headings")
        for c in cols:
            tree.heading(c, text=c)
            tree.column(c, width=120 if c != "note" else 360, anchor="w")
        tree.pack(fill="both", expand=True)
        if out.empty:
            tree.insert("", "end", values=["-", "-", "-", "-", "No outliers found"])
            return
        for _, r in out.iterrows():
            tree.insert("", "end", values=[
                r["id"],
                r["date"],
                r["category"],
                f"{float(r['amount']):.3f}",
                r["note"],
            ])

