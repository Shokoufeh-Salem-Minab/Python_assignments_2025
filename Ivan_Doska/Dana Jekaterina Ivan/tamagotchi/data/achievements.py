"""
This is achievement system for the Tamagotchi project.
"""

from tamagotchi import config

ACHIEVEMENTS = [

    # Age-based achievements
    {
        "name": "Childhood",
        "description": "Your pet reached age 5.",
        "condition": lambda pet, engine: len(engine.history) >= 5,
    },
    {
        "name": "Teen",
        "description": "Your pet reached age 10.",
        "condition": lambda pet, engine: len(engine.history) >= 10,
    },
    {
        "name": "Adult",
        "description": "Your pet reached age 20.",
        "condition": lambda pet, engine: len(engine.history) >= 20,
    },
    {
        "name": "Elder",
        "description": "Congratulations! Your pet reached age 100.",
        "condition": lambda pet, engine: len(engine.history) >= 100,
    },

    # Attribute 100% achievements
    {
        "name": "Happy 100",
        "description": "Your pet reached 100 happiness.",
        "condition": lambda pet, engine: pet.state[config.HAPPINESS] >= 100,
    },
    {
        "name": "Healthy 100",
        "description": "Your pet reached 100 health.",
        "condition": lambda pet, engine: pet.state[config.HEALTH] >= 100,
    },
    {
        "name": "Energy 100",
        "description": "Your pet reached 100 energy.",
        "condition": lambda pet, engine: pet.state[config.ENERGY] >= 100,
    },
    {
        "name": "Clean 100",
        "description": "Your pet reached 100 cleanliness.",
        "condition": lambda pet, engine: pet.state[config.CLEANLINESS] >= 100,
    },
]
