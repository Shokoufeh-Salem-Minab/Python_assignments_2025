FINANCE TRACKER – SEMESTER PROJECT
AUTHORS:
Matvey Zlatkvoskiy mz24039
Jānis Sniedze js23127
Asrin Uzay Coltu au24001
=================================

This is a desktop Finance Tracker application built in Python using Tkinter.
It allows users to manage income and expenses through a graphical interface
(no command line usage, no SQL database).
The project is modular and stores data locally using a CSV file.


System requirements:
--------------------
- Python 3.12.10
- Windows / macOS / Linux


What needs to be installed:
---------------------------
Python packages required:
- pandas
- matplotlib

Tkinter:
- Tkinter is included by default with standard Python installations
- No separate installation is required on Windows
- On Linux, I know you will find a bypass. You are smarter than Windows users

Example install command:
------------------------
Open a terminal / command prompt and run:

  pip install pandas matplotlib


How to run:
-----------
1. Make sure Python 3.12.10 is installed
2. Install required packages (see above)
3. Open the project folder
4. Run:

   python main.py

The application window should open.


Main features:
----------------------------
- Add income and expense transactions
- Edit existing transactions (one at a time)
- Delete one or multiple transactions
- Prevent invalid data:
  - Date must be YYYY-MM-DD
  - Date cannot be in the future
  - Amount must be a positive number
- Categories selected from a dropdown (no free typing)
- Transactions stored in CSV
- Automatic refresh (almost)

Transactions view:
------------------
- Table with filters:
  - Month
  - Type (income / expense)
  - Category
  - Amount range
  - Keyword search
- Multiple row selection for deletion
- Single-row edit only
- Summary statistics for filtered data

Dashboard / Visualization:
--------------------------
- Spending by category (pie chart)
- Income vs expense by month
- Daily expense trend
- Cumulative balance over time

Demo data:
----------
- "Generate Demo Data" button adds sample transactions
- Mostly expenses, some income
- Includes rare large expenses for visualization testing

Outliers:
---------
- Optional statistical feature
- Uses IQR (Interquartile Range) method
- Shows unusually large expenses

Project structure:
------------------
main.py                  Entry point
finance/
  app.py                 Main app layout & navigation
  config.py              Paths, constants, categories
  storage.py             CSV loading/saving
  analytics.py           Filtering, summaries, outliers
  plots.py               Charts and visualizations
  ui_home.py             Overview page
  ui_add_edit.py         Add/Edit transactions
  ui_transactions.py     Transactions table
  ui_dashboard.py        Charts page
data/
  transactions.csv       Stored data (auto-created)
logs/
  app.log                Application logs


