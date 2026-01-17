from __future__ import annotations

# Global configuration/constants for the Tamagotchi project.

# Stat bounds
STAT_MIN: int = 0
STAT_MAX: int = 100

# Stat indices for NumPy state vector:
# state = [health, hunger, energy, happiness, cleanliness]
HEALTH: int = 0
HUNGER: int = 1
ENERGY: int = 2
HAPPINESS: int = 3
CLEANLINESS: int = 4

STAT_NAMES = ["health", "hunger", "energy", "happiness", "cleanliness"]

# Initial values
DEFAULT_NAME: str = "Mochi"

START_STATS = {
    "health": 80,
    "hunger": 60,
    "energy": 70,
    "happiness": 65,
    "cleanliness": 70,
}

# Per-tick natural changes (applied each time step)
# Positive hunger means "more hungry" (worse), negative cleanliness means "dirtier" (worse).
TICK_DELTA = {
    "health": -1,
    "hunger": +4,
    "energy": -3,
    "happiness": -2,
    "cleanliness": -4,
}

# Action deltas (player commands). Values are deltas applied to the state.
# NOTE: shop/inventory/items are for teammate #2, so we keep only basic actions here.
ACTIONS = {
    "feed":       {"health": 0,  "hunger": -25, "energy": -2,  "happiness": +2, "cleanliness": -2},
    "play":       {"health": 0,  "hunger": +6,  "energy": -10, "happiness": +12, "cleanliness": -3},
    "sleep":      {"health": +2, "hunger": +8,  "energy": +25, "happiness": 0,   "cleanliness": 0},
    "clean":      {"health": 0,  "hunger": 0,   "energy": -2,  "happiness": +1, "cleanliness": +20},
    "heal":       {"health": +15,"hunger": +2,  "energy": -5,  "happiness": -1, "cleanliness": 0},
}

# Game rules thresholds
CRITICAL_HUNGER: int = 90
CRITICAL_DIRT: int = 20
LOW_ENERGY: int = 15
START_MONEY: int = 50
ACTION_REWARD: int = 2
TICK_REWARD: int = 0