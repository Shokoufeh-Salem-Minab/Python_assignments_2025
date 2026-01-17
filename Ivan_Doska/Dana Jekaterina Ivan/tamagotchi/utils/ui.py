from __future__ import annotations

from typing import List

from tamagotchi.models.pet import Pet


def format_stats_bar(value: int, width: int = 20) -> str:
    """Create a simple ASCII bar for a stat value."""
    value = max(0, min(100, int(value)))
    filled = int(round((value / 100) * width))
    return "[" + "#" * filled + "-" * (width - filled) + f"] {value:3d}"


def render_status(pet: Pet) -> str:
    """Return a formatted status string for the pet."""
    stats = pet.get_stats()

    lines = []
    lines.append(f"Pet: {pet.name} | Age (ticks): {pet.age}")
    lines.append("")
    for key in ["health", "hunger", "energy", "happiness", "cleanliness"]:
        lines.append(f"{key:12s} {format_stats_bar(stats[key])}")
    return "\n".join(lines)


def render_help() -> str:
    """Return a help message with available commands."""
    commands: List[str] = [
        "status                 - show pet status",
        "feed | play | sleep    - basic actions",
        "clean | heal           - basic actions",
        "next                   - pass time (tick)",
        "help                   - show this help",
        "quit                   - exit the game",
        "minigame               - start the minigame",
        "achievements           - shows achievements",
        "shop                   - opens shop",
        
        "NOTE: shop/inventory/items/achievements/minigame are for teammates.",
    ]
    return "\n".join(commands)
