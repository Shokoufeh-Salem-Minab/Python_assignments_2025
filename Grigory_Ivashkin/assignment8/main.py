
# csv is a standard Python library used to work with CSV files
import csv

# matplotlib.pyplot is used to draw charts (bar chart and pie chart)
import matplotlib.pyplot as plt


# list of categories we will track
CATEGORIES = ["Food", "Transport", "Clothes", "Entertainment"]

# number of days in a week
DAYS = 7


# this function safely gets a float number from user input
# it keeps asking until the user enters a valid non-negative number
def get_float_input(prompt):

    # infinite loop until correct input is given
    while True:

        # read user input as text
        # replace comma with dot so "10,5" also works
        text = input(prompt).strip().replace(",", ".")

        try:
            # try converting text to float
            value = float(text)

            # check that the number is not negative
            if value < 0:
                print("Please enter a non-negative number.")
            else:
                return value

        # if conversion to float fails
        except ValueError:
            print("Please enter a valid number.")


# main function that runs the whole program
def main():

    print("Weekly Expense Tracker")
    print("Categories:", ", ".join(CATEGORIES))
    print("We will enter expenses for 7 days.\n")

    # we use a dictionary:
    # key - category name (string)
    # value - list of daily expenses (7 numbers)
    #
    # e.g.
    # {
    #   "Food": [10, 12, 9, 11, 15, 8, 14],
    #   "Transport": [5, 6, 5, 7, 6, 5, 6]
    # }
    expenses = {}

    # initialize dictionary with empty lists
    for cat in CATEGORIES:
        expenses[cat] = []

    # outer loop: days
    # inner loop: categories
    for day in range(1, DAYS + 1):

        print(f"\n Day {day}")

        for cat in CATEGORIES:
            amount = get_float_input(f"{cat} expense: ")
            expenses[cat].append(amount)

    # ask user for weekly budget limit
    weekly_budget = get_float_input("\nEnter weekly budget limit: ")

    # calculate total expense for each category
    totals = {}
    for cat in CATEGORIES:
        totals[cat] = sum(expenses[cat])

    # calculate total expense for the whole week (all categories)
    total_week = sum(totals.values())

    # find category with highest total expense
    highest_category = None
    highest_value = -1

    for cat in CATEGORIES:
        if totals[cat] > highest_value:
            highest_value = totals[cat]
            highest_category = cat

    # calculate daily totals (sum of all categories per day)
    daily_totals = []

    for i in range(DAYS):
        day_sum = 0
        for cat in CATEGORIES:
            day_sum += expenses[cat][i]
        daily_totals.append(day_sum)

    # calculate daily average expense
    daily_average = sum(daily_totals) / DAYS

    # PRINT SUMMARY TO CONSOLE
    print("\n_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ ")
    print("\n Summary")

    for cat in CATEGORIES:
        print(f"{cat} total: {totals[cat]:.2f}")

    print("Highest category:", highest_category, f"({highest_value:.2f})")
    print(f"Total week expense: {total_week:.2f}")
    print(f"Daily average (all categories): {daily_average:.2f}")

    # BUDGET CHECK
    if total_week > weekly_budget:
        print("WARNING: Weekly budget exceeded!")
        print(f"Exceeded by: {(total_week - weekly_budget):.2f}")
    else:
        print("Weekly budget is OK.")

    # here we save the summary to CSV file
    csv_filename = "weekly_expenses_summary.csv"

    # open file in write mode
    with open(csv_filename, "w", newline="", encoding="utf-8") as f:

        # create CSV writer object
        writer = csv.writer(f)

        # header row
        writer.writerow(["Category", "Total"])

        # write totals per category
        for cat in CATEGORIES:
            writer.writerow([cat, f"{totals[cat]:.2f}"])

        # empty line for readability
        writer.writerow([])

        # additional summary rows
        writer.writerow(["TotalWeek", f"{total_week:.2f}"])
        writer.writerow(["DailyAverage", f"{daily_average:.2f}"])
        writer.writerow(["BudgetLimit", f"{weekly_budget:.2f}"])
        writer.writerow(["Exceeded", "YES" if total_week > weekly_budget else "NO"])

    print("\nSaved summary to:", csv_filename)

    # here we vizualise it through charts
    # bar chart shows total expenses per category
    categories = CATEGORIES
    values = [totals[cat] for cat in categories]

    plt.figure()
    plt.title("Weekly Expenses by Category (Total)")
    plt.bar(categories, values)
    plt.xlabel("Category")
    plt.ylabel("Total Expense")
    plt.tight_layout()
    plt.show()

    # pie chart shows how expenses are distributed between categories
    plt.figure()
    plt.title("Weekly Expenses Distribution")
    plt.pie(values, labels=categories, autopct="%1.1f%%")
    plt.tight_layout()
    plt.show()


# start the program
main()
