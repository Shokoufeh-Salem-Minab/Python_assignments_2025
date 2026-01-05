import pandas as pd
import matplotlib.pyplot as plt

# Initial data
categories = ["food", "transport", "clothes", "entertainment"]
days = 7

# Test data:
data = {
    "food": [13, 10, 1, 20, 25, 1, 3],
    "transport": [1.5, 1.5, 1.5, 1.5, 1.5, 1.5, 1.5],
    "clothes": [0, 10, 0, 25, 25, 1, 0],
    "entertainment": [100, 10, 0, 0, 0, 150, 220]
}

# Give user a choice to use test data or putting everything manually
print("Enter expenses manually? - 1")
print("Or use test data? - 2")
selected_mode = input("1 or 2?: ")

if (selected_mode == '1'):
    print("Enter daily expenses for 7 days:\n")

    # Ask user input for each category for each of the days (7 by default)
    for category in categories:
        expenses = []
        print(f"{category}:")
        for day in range(1, days + 1):
            value = float(input(f"Day {day}: "))
            expenses.append(value)
        data[category] = expenses
        print()

# Store data in a pd's dataframe
df = pd.DataFrame(data)
print("\nWeekly Expenses Table:")
print(df)

# Calculate a total per category
category_totals = df.sum()
print("\nTotal per category:")
print(category_totals)

# Calculate average spendings per day
daily_averages = df.mean()
print("\nDaily averages:")
print(daily_averages)

# Get category with highest expenses
highest_category = category_totals.idxmax()
print(f"\nHighest spending category: {highest_category}")

# Save summaries into a CSV file
category_totals.to_csv("Edgars_Spira/weekly_expenses_summary.csv")
print("\nSummary saved to weekly_expenses_summary.csv")



# Budget check
weekly_budget = float(input("\nEnter your weekly budget limit: "))
total_spent = category_totals.sum()

if total_spent > weekly_budget:
    print("Weekly budget exceeded!")
else:
    print("You are within your weekly budget.")


# Bar Chart
plt.figure(figsize=(6, 4))
category_totals.plot(kind="bar")
plt.title("Weekly Expenses by Category")
plt.ylabel("Amount Spent")
plt.tight_layout()
plt.show()

# Pie Chart
plt.figure(figsize=(6, 6))
category_totals.plot(kind="pie", autopct="%1.1f%%")
plt.title("Distribution of expenses")
plt.show()