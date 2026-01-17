"""
This is random events system for the Tamagotchi project.
"""

import random

class Event:
    def __init__(self, name, description, probability, delta: dict):
        self.name = name # Name of the event
        self.description = description
        self.probability = probability
        self.delta = delta  # Effect on the pet's stats (dictionary), passed to apply_delta()

    def apply(self, pet):
        pet.apply_delta(self.delta) # Apply stat changes to the pet
        return self.description # Return event description to be shown in logs


# Dictionary-based events
EVENTS = [
    Event(
        name="illness",
        description="Your pet feels sick. Energy and happiness decreased.",
        probability=0.06,
        delta={"hunger": 0, "happiness": -10, "energy": -15, "cleanliness": 0},
    ),
    Event(
        name="found_coins",
        description="Your pet found some coins! Happiness increased.",
        probability=0.08,
        delta={"hunger": 0, "happiness": +10, "energy": 0, "cleanliness": 0},
    ),
    Event(
        name="bad_mood",
        description="Your pet feels sad today.",
        probability=0.1,
        delta={"hunger": 0, "happiness": -5, "energy": -5, "cleanliness": 0},
    ),
    Event(
        name="good_mood",
        description="Your pet feels especially cheerful!",
        probability=0.09,
        delta={"hunger": 0, "happiness": +15, "energy": +10, "cleanliness": 0},
    ),
]


def trigger_random_event(pet):
    """Attempt to trigger a random event; return message or None."""
    for event in EVENTS:
        if random.random() < event.probability:
            msg = event.apply(pet) # Apply the event's stat effects to the pet
            return f"[Event: {event.name}] {msg}" # Return formatted log message for the engine
    return None
