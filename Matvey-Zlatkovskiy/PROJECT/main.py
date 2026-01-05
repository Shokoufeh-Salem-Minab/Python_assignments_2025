import sys

missing = []
try:
    import pandas  # type: ignore
except ImportError:
    missing.append(("pandas", "pip install pandas"))
try:
    import matplotlib  # type: ignore
except ImportError:
    missing.append(("matplotlib", "pip install matplotlib"))

if missing:
    for name, cmd in missing:
        print(f"Error: {name} not found. Please install it with this command: {cmd}")
    sys.exit(1)

from finance.app import FinanceTrackerApp


if __name__ == "__main__":
    app = FinanceTrackerApp()
    app.mainloop()
