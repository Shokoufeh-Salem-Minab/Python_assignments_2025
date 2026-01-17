from __future__ import annotations

from typing import Dict

from tamagotchi import config
from tamagotchi.models.pet import Pet


def get_tick_delta(pet: Pet) -> Dict[str, int]:
    """
    Calculate per-tick delta based on base decay + simple conditional rules.
    This is intentionally simple (advanced events will be done by next teammate #3).
    """
    delta = dict(config.TICK_DELTA)

    stats = pet.get_stats()

    # If hunger is critical, health decreases faster and happiness drops.
    if stats["hunger"] >= config.CRITICAL_HUNGER:
        delta["health"] -= 3
        delta["happiness"] -= 2

    # If cleanliness is too low, health decreases faster.
    if stats["cleanliness"] <= config.CRITICAL_DIRT:
        delta["health"] -= 2

    # If energy is very low, happiness decreases a bit more.
    if stats["energy"] <= config.LOW_ENERGY:
        delta["happiness"] -= 1

    return delta


def apply_tick(pet: Pet) -> None:
    """Apply one time step to the pet."""
    delta = get_tick_delta(pet)
    pet.apply_delta(delta)
    pet.tick_age()
