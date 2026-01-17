from __future__ import annotations
from tamagotchi.data.items import ITEMS
from tamagotchi import config
from tamagotchi.models.pet import Pet
from tamagotchi.engine.game import GameEngine
from tamagotchi.utils.ui import render_status, render_help
from tamagotchi.utils.validators import normalize_command


def render_shop(engine: GameEngine) -> str:
    lines = []
    lines.append(f"Money: {engine.money}$")
    lines.append("")

    for key, item in ITEMS.items():
        lines.append(f"{key:10s} | {item['price']:3d}$ | {item['description']}")

    lines.append("")
    lines.append("Commands: buy <item_name> | back")
    return "\n".join(lines)

def run() -> None:
    """Run the CLI Tamagotchi game loop."""
    pet = Pet(name=config.DEFAULT_NAME)
    engine = GameEngine(pet=pet)

    print("Welcome to TamaLab (CLI)!")
    print("Type 'help' to see commands.\n")

    while True:
        if not pet.is_alive():
            print("\nYour pet is not alive anymore. Game over.")
            break

        cmd = normalize_command(input("\n> "))

        if cmd in ("quit", "exit", "q"):
            print("Bye!")
            break

        if cmd in ("help", "h", "?"):
            print("\n" + render_help())
            continue

        if cmd in ("status", "stats"):
            print(f"\nMoney: {engine.money}$")
            print("\n" + render_status(pet))
            continue
        
        if cmd == "achievements":
            if not engine.achievements:
                print("\nNo achievements yet.")
            else:
                print("\nAchievements unlocked:")
                for a in engine.achievements:
                    print(" -", a)
            continue

        if cmd in ("next", "tick", "wait"):
            engine.tick()
            print("Time passed.")
            
            # Show ALL new events and achievements
            for entry in engine.logs[-3:]:  # check last few logs
                if entry.startswith("[Event:") or entry.startswith("[Achievement"):
                    print(entry)        
            continue
        
        if cmd in "shop":
            print("\n" + render_shop(engine))

            while True:
                sub = normalize_command(input("shop> "))

                if sub in ("back", "exit"):
                    break

                if sub.startswith("buy "):
                    item_name = sub.split(maxsplit=1)[1]
                    ok, msg = engine.buy_item(item_name)
                    print(msg)
                else:
                    print("Unknown shop command.")
            continue

        if cmd.startswith("use "):
            item_name = cmd.split(maxsplit=1)[1]
            ok, msg = engine.use_item(item_name)
            print(msg)
            continue
        
        if cmd == "minigame":
            print(engine.play_minigame())
            continue

        # Basic actions (your scope)
        ok, msg = engine.do_action(cmd)
        print(msg)
