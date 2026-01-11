from tkinter import ttk
from .analytics import summary_metrics
from .utils import compact_number

class HomeTab(ttk.Frame):
    def __init__(self, parent, app):
        super().__init__(parent)
        self.app = app
        self._build()

    def _build(self):
        outer = ttk.Frame(self, padding=16)
        outer.pack(fill="both", expand=True)
        title = ttk.Label(outer, text="Overview", style="Title.TLabel")
        title.pack(anchor="w", pady=(0, 10))
        self.cards = ttk.Frame(outer)
        self.cards.pack(fill="x", pady=(0, 12))
        self.lbl_income = self._card(self.cards, "Total Income", "0.000")
        self.lbl_expense = self._card(self.cards, "Total Expense", "0.000")
        self.lbl_net = self._card(self.cards, "Net", "0.000")
        self.lbl_avg = self._card(self.cards, "Avg Expense / Day", "0.000")
        note = ttk.Label(
            outer,
            text="Tip: Use filters in Transactions tab, then open Dashboard to visualize filtered data.",
            style="Muted.TLabel"
        )
        note.pack(anchor="w", pady=(10, 0))

    def _card(self, parent, title, value):
        card = ttk.Frame(parent, style="Card.TFrame", padding=12)
        card.pack(side="left", fill="x", expand=True, padx=6)
        ttk.Label(card, text=title, style="CardTitle.TLabel").pack(anchor="w")
        lbl = ttk.Label(card, text=value, style="CardValue.TLabel")
        lbl.pack(anchor="w", pady=(6, 0))
        return lbl

    def refresh(self):
        df = self.app.get_current_view_df()  # Uses current filters
        m = summary_metrics(df)
        self.lbl_income.config(text=compact_number(m['income']))
        self.lbl_expense.config(text=compact_number(m['expense']))
        self.lbl_net.config(text=compact_number(m['net']))
        self.lbl_avg.config(text=compact_number(m['avg_per_day']))
