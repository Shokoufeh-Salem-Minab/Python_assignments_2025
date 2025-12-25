"""
**You track expenses in the following categories:**

-Food
-Transport
-Clothes
-Entertainment

Each category contains daily expenses for one week (7 days).

**Your tasks are:**

Store the data using appropriate Python data structures
Calculate the total expense for each category
Find the category with the highest total expense
Save the summarized data into a CSV file
Visualize the expenses using a bar chart
Add user input for daily expenses
Calculate daily averages
Add a pie chart visualization
Set a weekly budget limit and display a warning if exceeded
"""

import csv

import matplotlib.pyplot as plt

COLORS = [
    "#FF0000",  # RED
    "#008000",  # GREEN
    "#4169E1",  # BLUE
    "#FFFF00",  # YELLOW
]


def get_expenses(categories: list[str]) -> dict[str, list[float]]:
    expenses = {}

    for category in categories:
        print(f"Enter expenses for {category}:")
        daily_expenses = []
        for day in range(1, 8):
            while True:
                try:
                    expense = float(input(f"\tDay {day}: "))
                    if expense < 0:
                        print("\tExpense could not be negative.")
                        continue
                    daily_expenses.append(expense)
                    break
                except ValueError:
                    print("\tInvalid input. Please enter a number.")
        expenses[category] = daily_expenses

    return expenses


def save_to_csv(
    expenses: dict[str, list[float]],
    totals: list[float],
    averages: list[float],
    filename="expenses.csv",
):
    with open(filename, "w", newline="") as csvfile:
        writer = csv.writer(csvfile)

        writer.writerow(
            [
                "Category",
                "Day 1",
                "Day 2",
                "Day 3",
                "Day 4",
                "Day 5",
                "Day 6",
                "Day 7",
                "Total",
                "Daily Average",
            ]
        )

        for category_idx, category in enumerate(expenses):
            row = (
                [category]
                + expenses[category]
                + [round(totals[category_idx], 2), round(averages[category_idx], 2)]
            )
            writer.writerow(row)


def display_and_save_barchart(
    expenses: dict[str, list[float]],
    totals: list[float],
):
    categories = list(expenses.keys())

    plt.figure(figsize=(10, 6))
    bars = plt.bar(
        categories,
        totals,
        color=COLORS,
    )

    for bar in bars:
        height = bar.get_height()
        plt.text(
            bar.get_x() + bar.get_width() / 2,
            height,
            f"{height:.2f}",
        )

    plt.xlabel("Categories")
    plt.ylabel("Expenses totals")
    plt.title("Expenses by category")
    plt.savefig("barchart.png")
    plt.show()


def display_and_save_piechart(
    expenses: dict[str, list[float]],
    totals: list[float],
):
    categories = list(expenses.keys())

    plt.figure(figsize=(8, 8))

    plt.pie(
        totals,
        labels=categories,
        autopct="%.2f%%",
        colors=COLORS,
    )

    plt.title("Expenses by category")
    plt.savefig("piechart.png")
    plt.show()


def main():
    # ask user budget limit
    while True:
        try:
            budget_limit = float(input("Enter your weekly budget limit: "))
            if budget_limit < 0:
                print("Budget limit could not be negative.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter a number.")

    expenses = get_expenses(["Food", "Transport", "Clothes", "Entertainment"])

    # get categories totals
    expenses_totals = []
    for category in expenses:
        expenses_totals.append(sum(expenses[category]))

    # find category with biggest total
    max_total_expense_category_idx = None

    for i in range(len(expenses_totals)):
        if (
            max_total_expense_category_idx is None
            or expenses_totals[i] > expenses_totals[max_total_expense_category_idx]
        ):
            max_total_expense_category_idx = i

    if max_total_expense_category_idx is None:
        raise RuntimeError("No categories were specified.")

    max_total_expense_category = list(expenses.keys())[max_total_expense_category_idx]
    print(f"Category with maximum total expense is: {max_total_expense_category}")

    # find daily averages
    daily_averages = []
    for day in range(7):
        day_total = sum(expenses[category][day] for category in expenses)
        daily_averages.append(day_total / len(expenses))

    print("\nDaily averages:")
    for day in range(7):
        print(f"\tDay {day + 1}: {daily_averages[day]:.2f}")

    # trigger warning if total expenses is bigger than budget limit
    if sum(expenses_totals) > budget_limit:
        print(
            f"Warning: budget limit is exceeded by {sum(expenses_totals) - budget_limit}"
        )

    # save info to csv
    save_to_csv(expenses, expenses_totals, daily_averages)
    # display and save as barchart
    display_and_save_barchart(expenses, expenses_totals)
    # display and save as piechart
    display_and_save_piechart(expenses, expenses_totals)


if __name__ == "__main__":
    main()
