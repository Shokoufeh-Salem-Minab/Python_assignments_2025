import os
import logging
import tkinter as tk
from tkinter import ttk
from .config import LOG_DIR, LOG_PATH, DEFAULT_CATEGORIES
from .storage import load_df
from .ui_home import HomeTab
from .ui_add_edit import AddEditTab
from .ui_transactions import TransactionsTab
from .ui_dashboard import DashboardTab

class FinanceTrackerApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Finance Tracker")
        self.geometry("1200x720")
        self.minsize(1100, 650)
        os.makedirs(LOG_DIR, exist_ok=True)
        logging.basicConfig(
            filename=LOG_PATH,
            level=logging.INFO,
            format="%(asctime)s | %(levelname)s | %(message)s",
        )
        self._setup_style()
        self._build_shell()
        self.refresh_all()

    def _setup_style(self):
        style = ttk.Style(self)
        # Try a nicer ttk theme if we can find one (whatever looks OK on this OS)
        # Matvey how the hell do you even call xpnative, Microslop killed it off. Who gonna be running this on XP?
        preferred = ["clam", "vista", "xpnative"]
        for t in preferred:
            if t in style.theme_names():
                style.theme_use(t)
                break
        style.configure("Title.TLabel", font=("Segoe UI", 16, "bold"))
        style.configure("Header.TLabel", font=("Segoe UI", 12, "bold"))
        style.configure("Muted.TLabel", foreground="#666666")
        # Card styles (simple boxed look)
        style.configure("Card.TFrame", relief="solid", borderwidth=1)
        style.configure("CardTitle.TLabel", font=("Segoe UI", 10), foreground="#444444")
        style.configure("CardValue.TLabel", font=("Segoe UI", 16, "bold"))
        # Sidebar styles (left nav area)
        style.configure("Sidebar.TFrame", padding=12)
        style.configure("Nav.TButton", padding=10)
        # Table heading style — ttk is annoying but this helps a bit
        style.configure("Treeview.Heading", font=("Segoe UI", 10, "bold"))
        # Table styling (make rows a bit taller so text doesn't look squashed)
        style.configure(
            "Treeview",
            font=("Segoe UI", 10),
            rowheight=30,
            borderwidth=0,
            relief="flat"
        )
        style.configure(
            "Treeview.Heading",
            font=("Segoe UI", 10, "bold"),
            padding=(6, 6)
        )
        # Selection colors so selected rows are visible
        style.map(
            "Treeview",
            background=[("selected", "#dbeafe")],
            foreground=[("selected", "black")]
        )
        # Tweak treeview layout so it looks cleaner
        style.layout("Treeview", [("Treeview.treearea", {"sticky": "nswe"})])
        
    def _build_shell(self):
        # Root container
        root = ttk.Frame(self)
        root.pack(fill="both", expand=True)
        # Sidebar (left buttons)
        self.sidebar = ttk.Frame(root, style="Sidebar.TFrame")
        self.sidebar.pack(side="left", fill="y")
        ttk.Label(self.sidebar, text="Finance Tracker", style="Header.TLabel").pack(anchor="w", pady=(0, 12))
        self.btn_home = ttk.Button(self.sidebar, text="Overview", style="Nav.TButton",
                                   command=lambda: self.show_page("home"))
        self.btn_add = ttk.Button(self.sidebar, text="Add / Edit", style="Nav.TButton",
                                  command=lambda: self.show_page("add"))
        self.btn_table = ttk.Button(self.sidebar, text="Transactions", style="Nav.TButton",
                                    command=lambda: self.show_page("table"))
        self.btn_dash = ttk.Button(self.sidebar, text="Dashboard", style="Nav.TButton",
                                   command=lambda: self.show_page("dash"))
        for b in [self.btn_home, self.btn_add, self.btn_table, self.btn_dash]:
            b.pack(fill="x", pady=4)
        ttk.Separator(self.sidebar).pack(fill="x", pady=12)
        ttk.Button(self.sidebar, text="Exit", command=self.destroy).pack(fill="x", pady=4)
        # Main area (header up top, content below)
        self.main = ttk.Frame(root, padding=10)
        self.main.pack(side="left", fill="both", expand=True)
        self.header = ttk.Frame(self.main, padding=(6, 6))
        self.header.pack(fill="x")
        self.lbl_title = ttk.Label(self.header, text="Overview", style="Title.TLabel")
        self.lbl_title.pack(side="left")
        self.lbl_quick = ttk.Label(self.header, text="", style="Muted.TLabel")
        self.lbl_quick.pack(side="right")
        ttk.Separator(self.main).pack(fill="x", pady=(6, 10))
        # Content pages container (we'll stack frames and lift the chosen one)
        self.pages = ttk.Frame(self.main)
        self.pages.pack(fill="both", expand=True)
        self.page_home = HomeTab(self.pages, self)
        self.page_add = AddEditTab(self.pages, self)
        self.page_table = TransactionsTab(self.pages, self)
        self.page_dash = DashboardTab(self.pages, self)
        self._page_map = {
            "home": self.page_home,
            "add": self.page_add,
            "table": self.page_table,
            "dash": self.page_dash,
        }
        for p in self._page_map.values():
            p.place(relx=0, rely=0, relwidth=1, relheight=1)
        self.show_page("home")
        
    def show_page(self, key: str):
        page = self._page_map[key]
        page.lift()
        titles = {
            "home": "Overview",
            "add": "Add / Edit",
            "table": "Transactions",
            "dash": "Dashboard",
        }
        self.lbl_title.config(text=titles.get(key, "Finance Tracker"))
        # refresh overview cards when showing home
        if key == "home":
            self.page_home.refresh()

    def refresh_all(self):
        df = load_df()
        # categories = defaults + whatever categories we find in the CSV
        data_cats = []
        if not df.empty:
            data_cats = df["category"].dropna().astype(str).str.strip().tolist()
        cats = sorted(set(DEFAULT_CATEGORIES) | set([c for c in data_cats if c]))
        self.page_add.set_categories(cats)
        self.page_table.set_categories(cats)
        self.page_table.refresh_table()
        # quick stats text (based on current view)
        m = self.page_table._get_filtered_view_df_metrics_for_header()
        self.lbl_quick.config(text=m)
        # keep overview up to date if it’s visible
        self.page_home.refresh()

    def start_edit(self, row_values: list):
        self.page_add.load_for_edit(row_values)
        self.show_page("add")

    def get_current_view_df(self):
        return self.page_table.get_filtered_view_df()

    def on_table_refreshed(self):
        # Update quick stats when filters/table changes
        m = self.page_table._get_filtered_view_df_metrics_for_header()
        self.lbl_quick.config(text=m)
        self.page_home.refresh()
