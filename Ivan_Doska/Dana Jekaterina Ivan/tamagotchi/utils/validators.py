from __future__ import annotations


def normalize_command(text: str) -> str:
    """Normalize user input into a lowercased command."""
    return (text or "").strip().lower()
