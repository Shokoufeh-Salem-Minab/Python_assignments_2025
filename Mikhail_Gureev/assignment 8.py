import csv
import matplotlib.pyplot as plt

# Expense categories
categories = ["Food", "Transport", "Clothes", "Entertainment"]

# Dictionary to store expenses
expenses = {}


# User input for 7 days

for category in categories:
    print(f"\nEnter expenses for {category} (7 days):")
    daily_expenses = []

    for day in range(1, 8):
        amount = float(input(f"Day {day}: "))
        daily_expenses.append(amount)

    expenses[category] = daily_expenses


# Calculate totals and averages

totals = {}
averages = {}

for category in categories:
    totals[category] = sum(expenses[category])
    averages[category] = totals[category] / 7


# Find highest spending category

highest_category = max(totals, key=totals.get)
print("\nHighest spending category:", highest_category)


# Weekly budget check

budget_limit = 500
weekly_total = sum(totals.values())

if weekly_total > budget_limit:
    print("⚠️ Warning: Weekly budget exceeded!")
else:
    print("✅ Weekly budget is within limit.")


# Save results to CSV file

with open("weekly_expenses.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Category", "Total Expense", "Daily Average"])

    for category in categories:
        writer.writerow([category, totals[category], averages[category]])

print("\nExpense summary saved to weekly_expenses.csv")

# Bar chart visualization

plt.bar(totals.keys(), totals.values())
plt.title("Weekly Expenses by Category")
plt.ylabel("Amount Spent")
plt.xlabel("Category")
plt.show()


# Pie chart visualization

plt.pie(totals.values(), labels=totals.keys(), autopct="%1.1f%%")
plt.title("Expense Distribution")
plt.show()
