import csv
import matplotlib.pyplot as plt

# List of expense categories
CATEGORIES = ["Food", "Transport", "Clothes", "Entertainment"]

# Number of days in the week
DAYS = 7

# Weekly budget limit
WEEKLY_BUDGET_LIMIT = 100

# Create a dictionary to store daily expenses for each category
expenses = {category: [] for category in CATEGORIES}

print("Enter daily expenses for each category, must fill 7 days:")

# Collect user input for 7 days per category
for category in CATEGORIES:
    print(category)
    for day in range(1, DAYS + 1):
        while True:
            try:
                # Input expense amount for the given day
                amount = float(input(f"Day {day}: "))
                # Reject negative values
                if amount < 0:
                    raise ValueError
                # Store valid expense
                expenses[category].append(amount)
                break
            except ValueError:
                # Handle invalid or negative input
                print("Error: expense cannot be negative or invalid. Please enter a number.")

# Dictionaries to store total and average expenses
total_expenses = {}
daily_averages = {}

# Calculate total and daily average for each category
for category, values in expenses.items():
    total_expenses[category] = sum(values)
    daily_averages[category] = total_expenses[category] / DAYS

# Calculate overall weekly expense
overall_total = sum(total_expenses.values())

print("\nYour weekly expenses:")

# Display total and average per category
for category in CATEGORIES:
    print(
        f"{category}: Total = {total_expenses[category]:.2f}, "
        f"Daily Average = {daily_averages[category]:.2f}"
    )

# Find the category with the highest spending
highest_category = max(total_expenses, key=total_expenses.get)
print(f"\nHighest spending category: {highest_category}")

# Display overall spending and budget status
print(f"\nOverall weekly spending: {overall_total:.2f}")
if overall_total > WEEKLY_BUDGET_LIMIT:
    print("WARNING: Weekly budget limit exceeded!")
else:
    print("Great! Weekly spending is within the budget.")

# Save summary data into a CSV file
with open("weekly_expense_summary.csv", "w", newline="") as file:
    writer = csv.writer(file)
    # Write header row
    writer.writerow(["Category", "Total Expense", "Daily Average"])
    # Write data rows for each category
    for category in CATEGORIES:
        writer.writerow([category, total_expenses[category], round(daily_averages[category], 2)])

# Create a bar chart to visualize total expenses
plt.bar(total_expenses.keys(), total_expenses.values())
plt.xlabel("Category")
plt.ylabel("Total Expense")
plt.title("Weekly Expenses by Category")
plt.show()

# Create a pie chart to visualize expense distribution
plt.pie(
    total_expenses.values(),
    labels=total_expenses.keys(),
    autopct="%1.1f%%",
    startangle=90
)
plt.title("Expense Distribution")
plt.show()
