import csv
import matplotlib.pyplot as plt

categories = ["Food", "Transport", "Clothes", "Entertainment"]
expenses = {cat: [] for cat in categories}
budgetLimit = 500
print(f"Your weekly budget is {budgetLimit}")

# Get user input for 7 days
for cat in categories:
    print(f"\nEnter daily expenses for {cat}: ")
    for day in range(1, 8):
        while True:
            try:
                val = float(input(f"Day {day}: "))
                break
            except ValueError:
                print("Enter a number.")
        expenses[cat].append(val)

catTotals = {cat: sum(vals) for cat, vals in expenses.items()}

totalWeek = sum(catTotals.values())
if totalWeek > budgetLimit:
    print(f"Warning: Weekly budget exceeded! Total = {totalWeek}")

maxCat = max(catTotals, key=catTotals.get)
print(f"\nCategory with highest total expense: {maxCat} ({catTotals[maxCat]})")

with open("assignment8/weekly_expenses.csv", "w", newline="") as f:
    catAverages = {cat: sum(vals)/7 for cat, vals in expenses.items()}
    writer = csv.writer(f)
    writer.writerow(["Category"] + [f"Day {i}" for i in range(1,8)] + ["Total", "Average"])
    for cat in categories:
        row = [cat] + expenses[cat] + [catTotals[cat], round(catAverages[cat],2)]
        writer.writerow(row)

# Bar chart of total expenses per category
plt.bar(categories, [catTotals[cat] for cat in categories])
plt.ylabel("Total Expense")
plt.title("Weekly Expenses by Category")
plt.show()

# Pie chart of expenses
plt.pie([catTotals[cat] for cat in categories], labels=categories, autopct="%1.1f%%")
plt.title("Expense Distribution")
plt.show()
