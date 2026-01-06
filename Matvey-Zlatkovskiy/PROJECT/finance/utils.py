import time
import logging

def log_action(action_name: str):
    def decorator(fn):
        def wrapper(*args, **kwargs):
            logging.info("ACTION: %s", action_name)
            return fn(*args, **kwargs)
        return wrapper
    return decorator

def timer(fn): # Decorator to time function execution
    def wrapper(*args, **kwargs):
        t0 = time.perf_counter()
        result = fn(*args, **kwargs)
        ms = (time.perf_counter() - t0) * 1000
        logging.info("TIMER: %s took %.3f ms", fn.__name__, ms)
        return result
    return wrapper


def compact_number(value) -> str:
    # Quick helper to make big numbers readable.
    # Example: 1231 -> '1.23k', 2500000 -> '2.50M'.
    # Common suffixes: k (thousand), M (million), B (billion), etc.
    try:
        v = float(value)
    except Exception:
        return str(value)
    sign = "-" if v < 0 else ""
    a = abs(v)
    # Units are given as 1e3, 1e6, etc. (that's 1000, 1_000_000, ...).
    # Map those to short suffixes so the UI isn't full of giant numbers.
    units = [
        (1e18, "E"),
        (1e15, "P"),
        (1e12, "T"),
        (1e9, "B"),
        (1e6, "M"),
        (1e3, "k"),
    ]
    for factor, suffix in units:
        if a >= factor:
            scaled = a / factor
            return f"{sign}{scaled:.2f}{suffix}"
    return f"{sign}{a:.3f}"
