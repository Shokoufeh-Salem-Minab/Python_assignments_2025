Layout Converter (RU ↔ EN)

This project is a Python application that converts text between
Russian and English keyboard layouts based on key positions.

Example:
You typed:
пщщв ьщктштп,

This app is capable of rewriting it as:
good morning?

The program supports:
- Manual and automatic direction detection (EN → RU, RU → EN)
- Windows-specific global hotkey (F8) to convert selected text
    If you want to change it, you need to change it on 690'th line of code.
- Graphical interface built with Tkinter

The program works on macOS, but global hotkeys are disabled there
due to OS-level limitations.

Files:
- app.py           — main application source code
- requirements.txt — required external Python packages

How to run:
1. Install Python 3.10+ on Windows.
2. Install dependencies:
   pip install -r requirements.txt
3. Run the application:
   python app.py

Note:
Tkinter is included with standard Python on Windows and does not need
to be installed separately.

The executable (.exe) version was created for personal use and can be
provided separately if required.
