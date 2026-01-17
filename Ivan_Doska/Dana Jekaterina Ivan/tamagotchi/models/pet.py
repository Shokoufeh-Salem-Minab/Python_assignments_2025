from __future__ import annotations

from dataclasses import dataclass, field
from typing import Dict, Any

import numpy as np

from tamagotchi import config


def _clamp(value: int, min_value: int = config.STAT_MIN, max_value: int = config.STAT_MAX) -> int:
    """Clamp an integer value into [min_value, max_value]."""
    return max(min_value, min(max_value, int(value)))


@dataclass
class Pet:
    """Core pet model storing its state as a NumPy vector."""

    name: str = config.DEFAULT_NAME
    age: int = 0  # number of ticks passed

    # NumPy state vector: [health, hunger, energy, happiness, cleanliness]
    state: np.ndarray = field(default_factory=lambda: Pet._state_from_dict(config.START_STATS))

    def __post_init__(self) -> None:
        """Initialize state if it was not provided or has wrong shape."""
        if self.state is None or not isinstance(self.state, np.ndarray) or self.state.shape != (5,):
            self.state = self._state_from_dict(config.START_STATS)

        self._clamp_state_inplace()

    @staticmethod
    def _state_from_dict(stats: Dict[str, int]) -> np.ndarray:
        """Build a NumPy state vector from a stats dict."""
        return np.array(
            [
                stats.get("health", config.START_STATS["health"]),
                stats.get("hunger", config.START_STATS["hunger"]),
                stats.get("energy", config.START_STATS["energy"]),
                stats.get("happiness", config.START_STATS["happiness"]),
                stats.get("cleanliness", config.START_STATS["cleanliness"]),
            ],
            dtype=int,
        )

    def _clamp_state_inplace(self) -> None:
        """Clamp all stats in the state vector to allowed bounds."""
        for i in range(self.state.shape[0]):
            self.state[i] = _clamp(self.state[i])

    def to_dict(self) -> Dict[str, Any]:
        """Serialize pet to a JSON-friendly dict."""
        return {
            "name": self.name,
            "age": self.age,
            "stats": self.get_stats(),
        }

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "Pet":
        """Create a Pet object from serialized dict."""
        name = data.get("name", config.DEFAULT_NAME)
        age = int(data.get("age", 0))

        stats = data.get("stats", {}) or {}
        state = cls._state_from_dict(stats)

        pet = cls(name=name, age=age, state=state)
        return pet

    def get_stats(self) -> Dict[str, int]:
        """Return current stats as a dict."""
        return {
            "health": int(self.state[config.HEALTH]),
            "hunger": int(self.state[config.HUNGER]),
            "energy": int(self.state[config.ENERGY]),
            "happiness": int(self.state[config.HAPPINESS]),
            "cleanliness": int(self.state[config.CLEANLINESS]),
        }

    def is_alive(self) -> bool:
        """Pet is alive if health is above minimum."""
        return int(self.state[config.HEALTH]) > config.STAT_MIN

    def apply_delta(self, delta: Dict[str, int]) -> None:
        """Apply a delta dict to the pet state."""
        self.state[config.HEALTH] += int(delta.get("health", 0))
        self.state[config.HUNGER] += int(delta.get("hunger", 0))
        self.state[config.ENERGY] += int(delta.get("energy", 0))
        self.state[config.HAPPINESS] += int(delta.get("happiness", 0))
        self.state[config.CLEANLINESS] += int(delta.get("cleanliness", 0))

        self._clamp_state_inplace()

    def tick_age(self) -> None:
        """Increase the pet's age counter by 1 tick."""
        self.age += 1
