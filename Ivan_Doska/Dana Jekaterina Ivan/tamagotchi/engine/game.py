from __future__ import annotations
from dataclasses import dataclass, field
from typing import List, Dict, Tuple, Optional
import numpy as np

from tamagotchi import config
from tamagotchi.models.pet import Pet
from tamagotchi.engine.rules import apply_tick
from tamagotchi.data.items import ITEMS
from tamagotchi.engine.events import trigger_random_event
from tamagotchi.data.achievements import ACHIEVEMENTS
from tamagotchi.engine.minigame import memory_game

@dataclass
class GameEngine:
    """Main game engine controlling the pet and time progression."""

    pet: Pet
    money: int = config.START_MONEY 
    inventory: Dict[str, int] = field(default_factory=dict)
    logs: List[str] = field(default_factory=list)
    achievements: List[str] = field(default_factory=list)

    # Stores snapshots of pet.state over time (NumPy arrays).
    history: List[np.ndarray] = field(default_factory=list)

    def __post_init__(self) -> None:
        self._snapshot("Game started.")

    def _snapshot(self, message: Optional[str] = None) -> None:
        """Store current state in history and optionally add a log message."""
        self.history.append(self.pet.state.copy())
        if message:
            self.logs.append(message)
            
    def check_achievements(self) -> None:
        """Check and unlock achievements."""
        for a in ACHIEVEMENTS:
            name = a["name"]

            if name in self.achievements:
                continue

            if a["condition"](self.pet, self):
                self.achievements.append(name)
                self.logs.append(f"[Achievement unlocked] {name}: {a['description']}")

    def tick(self) -> None:
        """Advance game time by one tick."""
        apply_tick(self.pet)
        self.money += config.TICK_REWARD
        self._snapshot("Time passed.")
        
        event_msg = trigger_random_event(self.pet)
        if event_msg:
            self.logs.append(event_msg)
        self.check_achievements()

    def do_action(self, action_name: str) -> Tuple[bool, str]:
        """
        Apply a player action if it exists.
        Returns (success, message).
        """
        action_name = action_name.strip().lower()

        if action_name not in config.ACTIONS:
            return False, f"Unknown action: '{action_name}'. Type 'help' to see commands."

        delta = config.ACTIONS[action_name]
        self.pet.apply_delta(delta)
        self.money += config.ACTION_REWARD
        self._snapshot(f"Action: {action_name}")
        return True, f"Done: {action_name}"

    def get_history_matrix(self) -> np.ndarray:
        """Return history as a matrix (ticks x stats)."""
        if not self.history:
            return np.zeros((0, 5), dtype=int)
        return np.vstack(self.history)

    def add_item(self, item_name: str, quantity: int = 1) -> None:
        """Add items to inventory."""
        if item_name not in ITEMS:
            raise ValueError(f"Unknown item: {item_name}")

        self.inventory[item_name] = self.inventory.get(item_name, 0) + quantity
        self.logs.append(f"Added {quantity} x {item_name}")

    def use_item(self, item_name: str) -> Tuple[bool, str]:
        """Use an item from inventory and apply its effect to the pet."""

        if item_name not in self.inventory or self.inventory[item_name] <= 0:
            return False, f"No item '{item_name}' in inventory."

        if item_name not in ITEMS:
            return False, f"Unknown item '{item_name}'."

        item = ITEMS[item_name]
        self.pet.apply_delta(item["effect"]) # Apply effect to pet
        self.inventory[item_name] -= 1 # Item was used/consumed

        if self.inventory[item_name] == 0:
            del self.inventory[item_name]

        self._snapshot(f"Used item: {item_name}")
        return True, f"Used {item['name']}"

    def buy_item(self, item_name: str) -> Tuple[bool, str]:
        item_name = item_name.lower()

        if item_name not in ITEMS:
            return False, f"Unknown item: {item_name}"

        item = ITEMS[item_name]
        price = item["price"]

        if self.money < price:
            return False, "Not enough money."

        self.money -= price
        self.inventory[item_name] = self.inventory.get(item_name, 0) + 1
        self.logs.append(f"Bought item: {item_name}")
        return True, f"Bought {item['name']} for {price}$"
    
    def play_minigame(self):
        """Run the memory mini-game defined in minigames.py."""
        return memory_game(self)
