# import sys is needed to determine the platform via sys.platform (Windows vs. macOS).
# In the case of our project, this affects the selection of mappings and the enabling/disabling of the global hotkey.
# This Windows application can automatically change the layout of selected text when you press F8. MacOS version can't.
import sys

# Import tkinter as tk is used to create application windows and widgets like Text.
# Importing under the name tk avoids typing tkinter.Text, tkinter.Tk, etc.
import tkinter as tk

# ttk stands for Themed Tk. These widgets (buttons, checkboxes, radio buttons, frames) have a more standard appearance than the "old" tk widgets.
# We use ttk for controls (Button, Checkbutton, Radiobutton, Frame), but retain tk.Text because ttk doesn't have a full-fledged multi-line text editor.
from tkinter import ttk

# import threading is needed to avoid blocking the GUI.
# pynput.Listener(...).join() is blocking. If you run it on the main thread, the window will freeze.
# Therefore, the hotkey listener and the worker (copy/paste/convert) are run in a separate thread.
import threading

# import time is used for small sleep(...) delays.
# They are necessary because copying the selection and updating the clipboard are not instant operations: 
# the OS/application may apply Ctrl+C a little later, and if you immediately read the clipboard, you could get the old value. 
# Alternatively, the keyboard layout change operations could take so long that nothing happens and we'll just get cv (from the copy-paste key combination).
import time

# from pynput import keyboard This is a library for:
# globally intercepting keys (F8), even when the focus is not in our window;
# programmatically sending keystrokes (Ctrl+C, Ctrl+V) via keyboard.Controller().
# Tkinter's built-in tools can't properly create a global hotkey outside of a window, so pynput is used.
# Without pynput, you can't create a global hotkey in other applications (Notepad, browser) using Tkinter.
# For the GUI, you could use PyQt / wxPython, but Tkinter is built into Python and is easier to install and compile into an .exe.
from pynput import keyboard


# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# 1) WINDOWS BASE MAPPINGS (RU <-> EN by key position)


# RU_TO_EN_LETTERS is a Python dictionary (type: dict).
# Dict literal syntax uses curly braces: {key: value, key: value, ...}
# Keys and values here are strings; each key/value is a 1-character string like "й" or "q".
# Dict lookup later is done by key: RU_TO_EN_LETTERS["й"] -> "q".
RU_TO_EN_LETTERS = {
    "й": "q", "ц": "w", "у": "e", "к": "r", "е": "t", "н": "y", "г": "u", "ш": "i", "щ": "o", "з": "p",
    "х": "[", "ъ": "]",
    "ф": "a", "ы": "s", "в": "d", "а": "f", "п": "g", "р": "h", "о": "j", "л": "k", "д": "l",
    "ж": ";", "э": "'",
    "я": "z", "ч": "x", "с": "c", "м": "v", "и": "b", "т": "n", "ь": "m",
    "б": ",", "ю": ".",
}

# EN_TO_RU_LETTERS is built automatically from RU_TO_EN_LETTERS using a dict comprehension.
# RU_TO_EN_LETTERS.items() returns an iterable of (key, value) pairs.
# "for k, v in ..." unpacks each pair into variables k and v.
# {v: k for ...} swaps them, creating the reverse mapping.
# Note: this assumes values are unique; otherwise later duplicates would overwrite earlier ones in the new dict.

# In simple terms, this line creates a new dictionary where the keys and values ​​are swapped
EN_TO_RU_LETTERS = {v: k for k, v in RU_TO_EN_LETTERS.items()}

# Another dict for punctuation/special symbols on Windows.
# Same dict literal syntax, still string->string mapping.
RU_TO_EN_PUNCT_WIN = {
    "ё": "`", "Ё": "~", "№": "#",
    ".": "/", ",": "?", "?": "&", "!": "!",
    ";": "$", "%": "%", ":": "^", "*": "*",
    "(": "(", ")": ")",
}

# Reverse punctuation map using the same dict comprehension pattern:
# iterate over (k, v) pairs and flip to (v, k).
EN_TO_RU_PUNCT_WIN = {v: k for k, v in RU_TO_EN_PUNCT_WIN.items()}



# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# 2) macOS FULL STRING-BASED MAPPING (RU <-> EN)

# These are "layout strings" for macOS. Each string is an ordered list of characters
# as they appear on the keyboard rows. We later convert them into dict mappings.
# Prefix r"" means a *raw string* in Python: backslashes are treated literally.
# Example: r"\'" keeps the backslash; useful when the string contains "\".
_MAC_EN_LETTERS = r"qwertyuiop[]asdfghjkl;'\zxcvbnm,./"
# Single quotes are used here because the string contains a double quote later in SHIFT row.
_MAC_EN_LETTERS_SHIFT = r'QWERTYUIOP{}ASDFGHJKL:"|ZXCVBNM<>?'

# Same idea, but for Russian layout characters on macOS.
_MAC_RU_LETTERS = r"йцукенгшщзхъфывапролджэёячсмитьбю/"
_MAC_RU_LETTERS_SHIFT = r"ЙЦУКЕНГШЩЗХЪФЫВАПРОЛДЖЭЁЯЧСМИТЬБЮ?"

# Number row on macOS is different from Windows, so we keep it separately.
# Again, raw strings: they are just constants, no special escape processing.
_MAC_EN_NUM = r"§1234567890-=`"
_MAC_EN_NUM_SHIFT = r"±!@#$%^&*()_+~"

# Russian number row for macOS.
_MAC_RU_NUM = r">1234567890-=]"
_MAC_RU_NUM_SHIFT = r'<!"№%5,.;()_+/'


# Helper function that builds a dictionary mapping character-by-character.
# Type hints: src: str, dst: str -> function expects strings.
# -> dict means it returns a dictionary (more precisely dict[str, str], but simplified here).

# Helper that converts two same-length "layout row" strings into a dict mapping.
# We store macOS layouts as ordered strings (RU row and the matching EN row), then build a character->character map automatically.
# This avoids writing dozens of manual pairs and makes the layout easy to edit/maintain.
def _build_map(src: str, dst: str) -> dict:

# Defensive check: mapping only works if both strings have the same length.
# len(...) returns the number of characters in a string.
    if len(src) != len(dst):

# raise ValueError(...) stops execution and reports an error with a message.
# f"..." is an f-string: it inserts expressions like {len(src)} into the string.
        raise ValueError(f"Layout strings must have the same length: {len(src)} != {len(dst)}")

# Dict comprehension:
# for i in range(len(src)) iterates i = 0..len(src)-1
# src[i] gets the i-th character of src, dst[i] gets the i-th character of dst
# result dict maps src[i] -> dst[i] for each position
# In simple terms, the function takes one character at a time from our strings of symbols and adds them one by one to a new dictionary,
#  letter by letter, each corresponding to its index in the string (e. g. qwertyuiop...)
    return {src[i]: dst[i] for i in range(len(src))}


# Start with an empty dict literal {} and then fill it step by step.
RU_TO_EN_PUNCT_MAC = {}

# dict.update(other_dict) merges keys/values from other_dict into this dict.
# If a key already exists, update overwrites the old value.
RU_TO_EN_PUNCT_MAC.update(_build_map(_MAC_RU_LETTERS, _MAC_EN_LETTERS))
RU_TO_EN_PUNCT_MAC.update(_build_map(_MAC_RU_LETTERS_SHIFT, _MAC_EN_LETTERS_SHIFT))

# Add base number-row mapping first.
RU_TO_EN_PUNCT_MAC.update(_build_map(_MAC_RU_NUM, _MAC_EN_NUM))

# Build shift-number mapping into a temporary dict.
# We do it separately because we DON'T want to overwrite digits that already exist.
_tmp_shift = _build_map(_MAC_RU_NUM_SHIFT, _MAC_EN_NUM_SHIFT)

# .items() iterates over (key, value) pairs in a dict.
# "for k, v in ..." unpacks each pair into variables k and v.
for k, v in _tmp_shift.items():

# "if k not in dict" checks whether the dict already has that key.
# This prevents overwriting existing mappings (especially digits).
    if k not in RU_TO_EN_PUNCT_MAC:

# standard dict assignment
        RU_TO_EN_PUNCT_MAC[k] = v

# Re-apply base number-row mapping to guarantee that digits stay correct.
RU_TO_EN_PUNCT_MAC.update(_build_map(_MAC_RU_NUM, _MAC_EN_NUM))

# Reverse mapping (EN -> RU) using dict comprehension.
EN_TO_RU_PUNCT_MAC = {v: k for k, v in RU_TO_EN_PUNCT_MAC.items()}

# Extra mapping for some uppercase Russian letters that correspond to shifted symbols on macOS.
# This is a plain dict literal. Used as a special-case override during conversion.
RU_TO_EN_SHIFT_SYMBOLS_MAC = {
    "Х": "{",
    "Ъ": "}",
    "Ж": ":",
    "Э": '"',
    "Б": "<",
    "Ю": ">",
    "Ё": "~",
}

# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# 3) OS DETECTION

# detect_platform() is a small helper function that returns a string label for the current OS.
# Syntax note: "def name(...) -> str:" means we define a function and annotate that it returns a string.
def detect_platform() -> str:

# sys.platform is a built-in Python string that identifies the OS in a short form.
# On macOS it is exactly "darwin".
    if sys.platform == "darwin":

# return exits the function immediately with this value
        return "mac"

# On Windows, sys.platform usually starts with "win" (for example "win32").
# .startswith("win") is a string method that checks the prefix.
    if sys.platform.startswith("win"):
        return "windows"

# Fallback: if the OS is something else (Linux, etc.), we treat it as Windows for our default behavior.
# (This keeps the app running with the Windows mapping instead of crashing.)
    return "windows"



# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# 4) CORE CONVERSION LOGIC

# convert_text takes a string and rewrites it character by character
# according to the selected direction and the current platform.
def convert_text(text: str, direction: str, platform: str) -> str:

# First we choose which mapping tables to use.
# macOS and Windows have different layouts and punctuation, so we switch here.
    if platform == "mac":
        ru_to_en_punct = RU_TO_EN_PUNCT_MAC
        en_to_ru_punct = EN_TO_RU_PUNCT_MAC
        ru_to_en_shift_symbols = RU_TO_EN_SHIFT_SYMBOLS_MAC
    else:
        ru_to_en_punct = RU_TO_EN_PUNCT_WIN
        en_to_ru_punct = EN_TO_RU_PUNCT_WIN
        ru_to_en_shift_symbols = {}

# We'll collect the converted characters into this list.
# Using a list is cheaper than concatenating strings in a loop.
    out = []

# Go through the input text one character at a time.
    for ch in text:

# lower() and isupper() are built-in string methods.
# This lets us handle uppercase letters without duplicating mappings.
        lower = ch.lower()
        is_upper = ch.isupper()

# Case 1: English -> Russian
        if direction == "en_to_ru":

# If the character exists in the letter mapping, replace it.
            if lower in EN_TO_RU_LETTERS:
                mapped = EN_TO_RU_LETTERS[lower]
                out.append(mapped.upper() if is_upper else mapped)

# After we've already added the completed character to out, there's no need to check any other conditions.
# Therefore, we exit the current iteration and move on to processing the next ch.
                continue

# Otherwise, try punctuation/special symbols.
            if ch in en_to_ru_punct:
                out.append(en_to_ru_punct[ch])
                continue


# Case 2: Russian -> English
        elif direction == "ru_to_en":

# macOS-specific fix: some uppercase Russian letters map to symbols.
            if ru_to_en_shift_symbols and ch in ru_to_en_shift_symbols:
                out.append(ru_to_en_shift_symbols[ch])
                continue

# Normal letter mapping.
            if lower in RU_TO_EN_LETTERS:
                mapped = RU_TO_EN_LETTERS[lower]

# Only letters can be uppercased; symbols are added as-is.
# is.alpha() is a check while the line is string.
                if mapped.isalpha():
                    out.append(mapped.upper() if is_upper else mapped)
                else:
                    out.append(mapped)
                continue

# Fallback to punctuation mapping.
            if ch in ru_to_en_punct:
                out.append(ru_to_en_punct[ch])
                continue

# If nothing matched, keep the original character unchanged.
        out.append(ch)

# Join the list into a single string and return it.
    return "".join(out)


# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# 5) AUTO DIRECTION DETECTION

# detect_direction tries to guess which way we should convert the text (EN->RU or RU->EN).
# It doesn't translate meaning, it just checks which "alphabet" the text looks closer to.
def detect_direction(text: str, lookahead: int = 40) -> str:

# .strip() removes spaces/newlines from both ends.
# We do this so "   " doesn't count as real input.
    s = text.strip()
    if not s:

# If the text is empty after stripping, default direction.
        return "en_to_ru"

# s[:lookahead] is Python slicing: take first N characters.
# We only analyze a small prefix so it stays fast even on huge pasted text.
    sample = s[:lookahead]

# set(...) creates a set object (unique elements, fast membership check: "x in set").
# EN_TO_RU_LETTERS.keys() gives all keys of the dict (like 'q', 'w', 'e', ...).
    en_keys = set(EN_TO_RU_LETTERS.keys())

# .update(...) adds multiple elements into the set.
# list("...") splits the string into a list of characters.
# Here we add common English-side punctuation keys.
    en_keys.update(list("[];'.,`/{}:\"|<>?"))

 # Same idea for Russian keys.
    ru_keys = set(RU_TO_EN_LETTERS.keys())
    ru_keys.update(list("ёЁ№"))

# Counters (ints). We'll count how many chars from the sample match each set.
    en_score = 0
    ru_score = 0

# Loop through sample one character at a time.
    for ch in sample:

# lower() so 'Q' and 'q' are treated the same.
        c = ch.lower()

# "in" on a set is fast: checks if c is one of the known layout characters.
        if c in en_keys:

# += 1 means "increase by 1"
            en_score += 1

        if c in ru_keys:
            ru_score += 1

# Ternary operator:
# if en_score >= ru_score -> return "en_to_ru" else return "ru_to_en"
    return "en_to_ru" if en_score >= ru_score else "ru_to_en"



# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# 6) GUI APPLICATION (Tkinter)


# App is the main window of the program.
# In Python, "class App(tk.Tk)" means inheritance: App extends Tkinter's Tk class.
# Practically: App already has all the window behavior (event loop, widgets, clipboard access),
# and we just add our own UI + hotkey logic on top.
class App(tk.Tk):

# These two are class-level constants (shared by all App instances).
# They are Windows Virtual-Key codes for the physical C and V keys.
# We use VK codes to send Ctrl+C / Ctrl+V in a way that does NOT depend on the current keyboard layout.
# That's important because with a Russian layout active, sending 'c' / 'v' as characters may not behave as intended.
    _VK_C = 0x43
    _VK_V = 0x56

    def __init__(self):

# super().__init__() runs tk.Tk constructor.
# Without it, Tkinter won't initialize the window, clipboard API, and internal event system correctly.
        super().__init__()

# Basic window setup: visible title + default size.
# geometry("780x540") sets initial width/height, and minsize prevents collapsing the UI.
        self.title("Layout Converter (RU ↔ EN)")
        self.geometry("780x540")
        self.minsize(720, 500)

# Detect OS once and store it.
# We use this later to pick the correct layout mappings (Windows vs macOS)
# and to decide whether global hotkey should work (Windows only).
        self.platform = detect_platform()

# Tkinter Variables:
# They are special wrapper objects that widgets can "bind" to.
# When a user clicks a checkbox/radiobutton, these variables update automatically.
# And when we change the variable in code, the widget state updates too.

# auto_var: whether direction is auto-detected or manually selected.
        self.auto_var = tk.BooleanVar(value=True)

# manual_dir_var: stores the manual mode direction string: "en_to_ru" or "ru_to_en".
        self.manual_dir_var = tk.StringVar(value="en_to_ru")

# Hotkey state:
# _hotkey_enabled: master switch controlled by the UI checkbox.
# _hotkey_busy: prevents re-entry (user can press F8 multiple times fast; we ignore while working).
# _hotkey_listener: will hold the pynput listener object so we can track it if needed.
# _hotkey_last_ts: timestamp used for debounce (cooldown between triggers).
        self._hotkey_enabled = True
        self._hotkey_busy = False
        self._hotkey_listener = None
        self._hotkey_last_ts = 0.0

# Status message control:
# We show short messages like "Copied to clipboard".
# Tkinter's after() returns an id; we store it so we can cancel a previous "clear status" timer.
        self._status_after_id = None

# Build UI widgets (text areas, buttons, checkboxes) and bind callbacks.
        self._build_ui()

# Start global hotkey handling.
# On Windows it listens for F8 globally (even outside the app).
# On macOS in our current version it should disable itself inside _start_hotkey_listener().
        self._start_hotkey_listener()



# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# 7) UI 

    def _build_ui(self):

# root is the main container frame inside the window (self is tk.Tk).
# padding=12 adds inner space so widgets don't stick to the window edges.
        root = ttk.Frame(self, padding=12)
# pack() is one of Tkinter's layout managers.
# fill="both" makes it stretch horizontally+vertically, expand=True lets it grow with the window.
        root.pack(fill="both", expand=True)

# controls is the top bar: checkboxes + radiobuttons.
        controls = ttk.Frame(root)

# fill only horizontally
        controls.pack(fill="x")

# Checkbutton is linked to self.auto_var (a tk.BooleanVar).
# When the user toggles it, auto_var becomes True/False automatically.
# command=self._reconvert_if_needed means: after click, run this method.
        ttk.Checkbutton(
            controls, text="Auto direction",
            variable=self.auto_var, command=self._reconvert_if_needed
        ).pack(side="left")

# Radiobuttons share the same variable (self.manual_dir_var).
# value="en_to_ru" means: if this radio is selected, manual_dir_var becomes "en_to_ru".
# command triggers reconversion so UI updates immediately.
        ttk.Radiobutton(
            controls, text="EN → RU", value="en_to_ru",
            variable=self.manual_dir_var, command=self._reconvert_if_needed
        ).pack(side="left", padx=(12, 0)) # padx adds horizontal spacing (left,right)

        ttk.Radiobutton(
            controls, text="RU → EN", value="ru_to_en",
            variable=self.manual_dir_var, command=self._reconvert_if_needed
        ).pack(side="left", padx=(8, 0)) 

# A visual separator line between direction controls and hotkey switch.
        ttk.Separator(controls, orient="vertical").pack(side="left", fill="y", padx=12)

# Separate variable for enabling/disabling the global hotkey.
# This is not the same as auto direction — it's only about the F8 feature.
        self.hotkey_var = tk.BooleanVar(value=True)
        ttk.Checkbutton(
            controls, text="Global hotkey enabled",
            variable=self.hotkey_var, command=self._toggle_hotkey
        ).pack(side="left")

# body is the main area with two text boxes: input and output.
        body = ttk.Frame(root)
        body.pack(fill="both", expand=True, pady=(12, 0))

# We use grid layout inside body because it's a clean 2-column layout.
# weight=1 means the columns stretch evenly when the window resizes.
        body.columnconfigure(0, weight=1)
        body.columnconfigure(1, weight=1)

# row 1 is where the Text widgets are; weight=1 makes them expand vertically.
        body.rowconfigure(1, weight=1)

# Labels above each text box.
        ttk.Label(body, text="Input").grid(row=0, column=0, sticky="w")
        ttk.Label(body, text="Output").grid(row=0, column=1, sticky="w", padx=(10, 0))

# tk.Text is a multiline editor widget (ttk doesn't have a real equivalent).
# wrap="word" means it wraps by words instead of splitting words in the middle.
        self.input_text = tk.Text(body, wrap="word", height=18)
        self.output_text = tk.Text(body, wrap="word", height=18)

# We disable output_text so it's read-only (user can't accidentally edit the result).
        self.output_text.configure(state="disabled")

# sticky="nsew" means stretch to all directions in the grid cell (north/south/east/west).
        self.input_text.grid(row=1, column=0, sticky="nsew")
        self.output_text.grid(row=1, column=1, sticky="nsew", padx=(10, 0))

# Bind copy/paste/select-all shortcuts for both text widgets.
# Reason: different platforms/apps can behave differently, we force consistent shortcuts.
        self._bind_text_shortcuts(self.input_text)
        self._bind_text_shortcuts(self.output_text)

# Bottom button row.
        buttons = ttk.Frame(root)
        buttons.pack(fill="x", pady=(12, 0))

# Button command=... means "call this method when clicked".
# Convert also copies result to clipboard; Clear wipes both fields.
        ttk.Button(buttons, text="Convert (and copy)", command=self.on_convert).pack(side="left")
        ttk.Button(buttons, text="Clear", command=self.on_clear).pack(side="right")

# Small hint label so user knows what the hotkey is.
# On macOS in our current version hotkey is disabled, on Windows it's F8.
        if self.platform == "mac":
            hint_text = "Hotkey (macOS): disabled"
        else:
            hint_text = "Hotkey (Windows): F8 — converts selected text and replaces it (auto direction)"

        hint = ttk.Label(root, text=hint_text)
        hint.pack(fill="x", pady=(10, 0))

# Status line at the bottom ("Copied to clipboard", etc.)
# textvariable links a Label to a StringVar: updating the variable updates the label automatically.
        self.status_var = tk.StringVar(value="")
        self.status_label = ttk.Label(root, textvariable=self.status_var)
        self.status_label.pack(fill="x", pady=(6, 0))

    def _bind_text_shortcuts(self, widget: tk.Text):

# Small helper generator: returns a handler function that triggers a Tk virtual event.
# This lets us map multiple key combos (Ctrl+C and Cmd+C) to the same action.
        def gen(ev_name):
            def _handler(_e):

# event_generate creates a virtual event like "<<Copy>>"
# Tk knows how to execute these standard events for Text widgets.
                widget.event_generate(ev_name)

# stops default handling so we don't get double actions
                return "break"
            return _handler

# macOS-style shortcuts
        widget.bind("<Command-c>", gen("<<Copy>>"))
        widget.bind("<Command-v>", gen("<<Paste>>"))
        widget.bind("<Command-x>", gen("<<Cut>>"))
        widget.bind("<Command-a>", gen("<<SelectAll>>"))

# Windows/Linux-style shortcuts
        widget.bind("<Control-c>", gen("<<Copy>>"))
        widget.bind("<Control-v>", gen("<<Paste>>"))
        widget.bind("<Control-x>", gen("<<Cut>>"))
        widget.bind("<Control-a>", gen("<<SelectAll>>"))


# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# 8) Helpers 

    def _toggle_hotkey(self):

# hotkey_var is a Tk BooleanVar connected to the "Global hotkey enabled" checkbox.
# .get() returns its current value (True/False, sometimes 0/1).
# bool(...) normalizes it to a real Python bool.

# We also hard-limit hotkeys to Windows only:
# even if someone toggles the checkbox on macOS, _hotkey_enabled will still be False.
        self._hotkey_enabled = bool(self.hotkey_var.get()) and (self.platform == "windows")

    def _reconvert_if_needed(self):

# Read full text from the input Text widget.
# "1.0" means line 1, character 0 (start of the widget).
# "end-1c" means "end minus 1 character" (Tk adds a trailing newline at 'end', we exclude it).
        inp = self.input_text.get("1.0", "end-1c")

# .strip() removes whitespace around.
# If something real exists, we rerun conversion immediately.
# This is used when user toggles auto/manual direction buttons.
        if inp.strip():
            self.on_convert()

    def _effective_direction(self, text: str) -> str:

# auto_var is a Tk BooleanVar linked to the "Auto direction" checkbox.
# If auto is enabled -> call detect_direction(text) to guess the direction.
# If auto is disabled -> take manual_dir_var value ("en_to_ru" or "ru_to_en") from radiobuttons.
        return detect_direction(text) if self.auto_var.get() else self.manual_dir_var.get()

    def _status(self, msg: str, ms: int = 1400):

# We show short status messages in the bottom label (like "Copied to clipboard").
# The tricky part: if user triggers actions quickly, we don't want multiple timers fighting.

# self.after(...) returns an id. If a previous "clear message" timer exists,
# we cancel it first, then schedule a new one.
        if self._status_after_id is not None:
            try:

# after_cancel cancels the scheduled callback by its id.
                self.after_cancel(self._status_after_id)
            except Exception:

# if it was already executed/cancelled, ignore.
                pass
            self._status_after_id = None

# status_var is a StringVar connected to the label via textvariable=...
# Updating it updates the UI label automatically.
        self.status_var.set(msg)

# If ms > 0, schedule clearing the status after ms milliseconds.
# lambda is an anonymous function used here as a tiny callback.
        if ms > 0:
            self._status_after_id = self.after(ms, lambda: self.status_var.set(""))

    def _hotkey_debounce_ok(self, min_interval_sec: float = 0.45) -> bool:

# Debounce = ignore repeated triggers too quickly.
# time.time() returns current timestamp in seconds (float).
        now = time.time()

# If the last trigger was less than min_interval_sec ago, reject this trigger.
        if now - self._hotkey_last_ts < min_interval_sec:
            return False
        
# Otherwise accept, and store the timestamp.        
        self._hotkey_last_ts = now
        return True

# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# 9) Main actions 

    def on_convert(self):

# Read input from input Text widget (same "1.0" / "end-1c" logic).
        inp = self.input_text.get("1.0", "end-1c")

# If input is empty/whitespace, show message and exit.
        if not inp.strip():
            self._status("Nothing to convert", ms=1200)
            return

# Decide direction (auto or manual) and run conversion.
        direction = self._effective_direction(inp)
        out = convert_text(inp, direction=direction, platform=self.platform)

# Output Text is read-only, so we temporarily enable it to update the content.
        self.output_text.configure(state="normal")

# delete everything
        self.output_text.delete("1.0", "end")

# insert new result at the start
        self.output_text.insert("1.0", out)
        self.output_text.configure(state="disabled")

# If output is non-empty, copy it to clipboard and show status.
# _safe_clipboard_set is used because clipboard access must happen in the Tk main thread.
        if out.strip():
            self._safe_clipboard_set(out)
            self._status("Copied to clipboard")
        else:
            self._status("Conversion result is empty", ms=1200)

    def on_clear(self):

# Clear input text.
        self.input_text.delete("1.0", "end")

# Clear output text (again: enable -> edit -> disable).
        self.output_text.configure(state="normal")
        self.output_text.delete("1.0", "end")
        self.output_text.configure(state="disabled")

# Clear status line too.
        self._status("")
# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# 10) Hotkey listener

    def _start_hotkey_listener(self):

# If we are not on Windows, we just disable the hotkey checkbox and exit.
# This way macOS still works as a normal GUI converter, just without global hotkeys.
        if self.platform != "windows":

# update the UI checkbox state
            self.hotkey_var.set(False)

# internal flag so nothing triggers
            self._hotkey_enabled = False
            return

# This is the function that will run inside a background thread.
# Reason: keyboard.Listener(...).join() blocks forever, so we can't run it in the Tk main thread.
        def run_listener():

# Callback for each key press captured globally by pynput.
# Parameter k is a Key object (like keyboard.Key.f8) or KeyCode.
            def on_press_win(k):

# If user disabled the hotkey in the UI, ignore.
                if not self._hotkey_enabled:
                    return

# If F8 was pressed and debounce allows it, trigger the selection conversion.
# self.after(0, ...) is important: it schedules the call on Tk's main thread.
# Tkinter is not thread-safe, so we avoid touching UI from the listener thread.
                if k == keyboard.Key.f8 and self._hotkey_debounce_ok():
                    self.after(0, self._trigger_selection_convert)

# Start listening globally.
# "with ... as listener" keeps the listener alive and guarantees cleanup on exit.
# listener.join() blocks the thread and keeps listening until the app exits.
            with keyboard.Listener(on_press=on_press_win) as listener:
                self._hotkey_listener = listener
                listener.join()

# Start the listener in daemon thread:
# daemon=True means it won't prevent the program from exiting.
        threading.Thread(target=run_listener, daemon=True).start()


    def _trigger_selection_convert(self):

# Prevent running multiple conversions at the same time.
# Without this, spam pressing F8 could start many threads that fight over clipboard.
        if self._hotkey_busy:
            return
        self._hotkey_busy = True

# Real work is done in a worker thread because we do sleeps + clipboard work,
# and we don't want the GUI to freeze.
        def worker():
            try:

# Save current clipboard so we can restore it after replacing the selection.
                old_clip = self._safe_clipboard_get()

# Send Ctrl+C using VK codes (layout-independent).
# This is the fix for the "cv" bug when RU layout is active.
                self._send_copy_windows_vk()
                time.sleep(0.12)  # give the OS/app time to update clipboard

# Read selected text from clipboard.
                selected = self._safe_clipboard_get()
                if not selected.strip():

# nothing selected, nothing to convert
                    return

# Decide direction (auto/manual) and convert.
                direction = self._effective_direction(selected)
                converted = convert_text(selected, direction=direction, platform=self.platform)
                if not converted.strip():
                    return

# Put converted text into clipboard and paste back over the selection.
                self._safe_clipboard_set(converted)
                time.sleep(0.03)
                self._send_paste_windows_vk()

# Restore user's clipboard (so we don't permanently overwrite their copied content).
                time.sleep(0.12)
                self._safe_clipboard_set(old_clip)

            finally:

# Always release the busy flag even if something fails.
                self._hotkey_busy = False

        threading.Thread(target=worker, daemon=True).start()

# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# 11) Clipboard helpers

    def _clipboard_get_mainthread(self) -> str:

# This is the "direct" clipboard read using Tkinter.
# Important: Tkinter clipboard calls should happen on the Tk main thread.
        try:

# clipboard_get() returns current clipboard text (string).
            return self.clipboard_get()
        except tk.TclError:

# Tk can throw TclError if clipboard is empty or not text.
            return ""


    def _clipboard_set_mainthread(self, text: str):

# This is the "direct" clipboard write using Tkinter (also should be main thread).
        try:

# Clear first, then append new text.
            self.clipboard_clear()
            self.clipboard_append(text)

# update_idletasks() forces Tk to process pending UI tasks.
# Here it helps to "flush" clipboard updates so they apply immediately.
            self.update_idletasks()
        except tk.TclError:

# If clipboard fails for some reason, we just ignore (best-effort).
            pass


    def _safe_clipboard_get(self) -> str:

# This wrapper makes clipboard read safe from ANY thread.
# If we are already on the main thread -> just call the direct function.
        if threading.current_thread() is threading.main_thread():
            return self._clipboard_get_mainthread()

# If we are in a worker thread, we can't touch Tk directly.
# So we schedule a small "run" function to execute on the main thread via self.after(...).

# mutable container to store result from the main thread
        box = {"val": ""}

# event used to wait until the main-thread task finishes
        ev = threading.Event()

        def run():

# This runs in the Tk main thread.
            box["val"] = self._clipboard_get_mainthread()

# signal that the result is ready
            ev.set()

# self.after(0, run) queues the function in Tk's event loop ASAP.
        self.after(0, run)

# Worker thread waits until main thread finishes reading clipboard.
# timeout avoids infinite freeze if something goes wrong.
        ev.wait(timeout=1.0)

# Return what main thread put into box.
        return box["val"]


    def _safe_clipboard_set(self, text: str):

# Same concept but for writing.
# If we are on main thread -> write directly.
        if threading.current_thread() is threading.main_thread():
            self._clipboard_set_mainthread(text)
            return

# If we are in a worker thread -> schedule the clipboard write on the main thread and wait.
        ev = threading.Event()

        def run():
            self._clipboard_set_mainthread(text)
            ev.set()

        self.after(0, run)
        ev.wait(timeout=1.0)

# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# 12) Key helpers

    def _send_copy_windows_vk(self):

# Create a keyboard controller object from pynput.
# It can simulate key presses globally (not only inside our window).
        kc = keyboard.Controller()

# keyboard.Key.ctrl is a special constant representing the Ctrl modifier key.
        ctrl = keyboard.Key.ctrl

# KeyCode.from_vk(...) creates a KeyCode using a Windows virtual-key code.
# We use VK_C (0x43) instead of the character 'c' so it's layout-independent.
# This is exactly the fix for the "cv" issue when RU layout is active.
        key_c = keyboard.KeyCode.from_vk(self._VK_C)

# try/finally is used so Ctrl is ALWAYS released, even if something errors mid-way.
        try:

# Press and hold Ctrl
            kc.press(ctrl)

# small delay so OS registers modifier down
            time.sleep(0.01)

# Press and release C while Ctrl is held -> Ctrl+C
            kc.press(key_c)
            kc.release(key_c)
            time.sleep(0.01)
        finally:

# Release Ctrl no matter what.
# Nested try because releasing can sometimes throw if OS state is weird.
            try:
                kc.release(ctrl)
            except Exception:
                pass


    def _send_paste_windows_vk(self):

# Same structure as copy, but with V instead of C.
        kc = keyboard.Controller()
        ctrl = keyboard.Key.ctrl

# VK_V (0x56) is the physical V key.
# Ctrl + VK_V -> paste, independent of current keyboard layout.
        key_v = keyboard.KeyCode.from_vk(self._VK_V)

        try:
            kc.press(ctrl)
            time.sleep(0.01)

            kc.press(key_v)
            kc.release(key_v)
            time.sleep(0.01)
        finally:
            try:
                kc.release(ctrl)
            except Exception:
                pass

# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# finally

# This block makes the file runnable as a script.
# In Python, __name__ is a special variable:
# - if we run this file directly (python app.py), then __name__ == "__main__"
# - if we import this file as a module, __name__ will be the module name, not "__main__"
if __name__ == "__main__":
    # Create the GUI window (runs App.__init__ and builds the whole interface).
    app = App()

    # Start Tkinter event loop.
    # mainloop() keeps the window alive, listens for clicks/keys, and calls our callbacks.
    # When the window is closed, mainloop() returns and the program exits.
    app.mainloop()
