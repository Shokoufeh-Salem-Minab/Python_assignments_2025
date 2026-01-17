"""
This mini-game trains your memory by showing a matrix full of numbers.
You must memorize the entire matrix and then type it back row by row.

The rules:
- The matrix appears for 3 seconds.
- Then the console clears.
- You must rewrite the matrix exactly as shown earlier.
- Each level increases the matrix size (up to 6x6).
- Correct answer → +10$ reward.
- Wrong answer → you may restart the game or exit.

IMPORTANT:
To exit the game type 'exit', after game loss you can choose continue or exit the game.
"""

import numpy as np
import time
import os

def print_matrix(matrix):
    """Print matrix row by row without NumPy brackets."""
    for row in matrix:
        print(" ".join(str(num) for num in row))


def clear_console():
    """Clear the terminal screen for both Windows ('cls') and Linux/Mac ('clear')."""
    os.system("cls" if os.name == "nt" else "clear")


def memory_game(engine):
    
    print("\n    MEMORY MATRIX GAME    ")
    print("You will see a matrix for 3 seconds.")
    print("Memorize it and type it back row by row.")
    print("Earn +10$ for every correct matrix.")
    print("If you lose, you may restart or exit.\n")
    print("TIP: Type 'exit' at ANY time to leave the mini-game.\n")

    # FIRST INPUT – allow exit before game starts
    begin = input("Press Enter to begin... ").strip().lower()
    if begin == "exit":
        return "Exiting mini-game... Returning to main menu."

    # Outer loop allows restarting the mini-game from Level 1
    while True:

        level = 1  # reset game progression on restart

        # Level loop
        while True:
            # Determine matrix size (grows each level)
            size = min(1 + level, 6)

            # Generate random matrix (digits 0–9)
            matrix = np.random.randint(0, 10, (size, size))

            print(f"\nLevel {level}")
            print("Memorize this matrix:\n")
            print_matrix(matrix)

            # Show matrix for 3 seconds
            time.sleep(3)

            # Hide matrix
            clear_console()

            print(f"Matrix size: {size}x{size}")
            print("Enter each row exactly as shown before.")
            print("Example of correct input for a row: 1 5 3")
            print("Remember: type 'exit' anytime to quit.\n")

            user_matrix = []

            # Collect rows from the player
            for row_index in range(size):
                row_input = input(f"Row {row_index + 1}: ").strip()

                # Allow global exit keyword
                if row_input.lower() == "exit":
                    return "Exiting mini-game... Returning to main menu."

                # Convert input string to a list of integers
                try:
                    numbers = [int(n) for n in row_input.split()]
                except ValueError:
                    print("\nInput contained non-numbers. Game over.")
                    break  # goes to post-loss prompt

                # Ensure the player entered the correct number of values
                if len(numbers) != size:
                    print("\nRow length mismatch. Game over.")
                    break

                user_matrix.append(numbers)

            else:
                # This block executes only if NO break occurred in the loop above
                user_matrix = np.array(user_matrix)

                # Compare player's matrix with the original matrix
                if np.array_equal(user_matrix, matrix):
                    reward = 10
                    engine.money += reward
                    engine.logs.append(
                        f"[Mini-game] Level {level} completed (+{reward}$)"
                    )
                    print("\nCorrect!")
                    print(f"You earned +{reward}$!")
                    level += 1
                    continue  # proceed to next level

                # If matrices do not match
                print("\nThat matrix was incorrect.")
                engine.logs.append("[Mini-game] Incorrect matrix")

            # LOSS SCREEN 
            print(f"\nYou reached Level {level}.")
            print("Choose an option:")
            print("  1) Restart the mini-game from Level 1")
            print("  2) Exit to the main Tamagotchi menu\n")

            choice = input("Enter 1 or 2: ").strip().lower()

            if choice == "exit" or choice == "2":
                return "Exiting mini-game... Returning to main menu."

            # Otherwise restart mini-game
            print("\nRestarting mini-game...\n")
            break  # restart from Level 1
