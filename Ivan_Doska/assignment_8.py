import csv
import matplotlib.pyplot as plt

CATEGORIES = ["Food", "Transport", "Clothes", "Entertainment"]
DAYS = 7
WEEKLY_BUDGET_LIMIT = 300.0  
expenses = {} # global variable
print("Enter daily expenses for each category (7 days):\n")

for category in CATEGORIES:
    daily = []
    print(f"{category}:")
    for day in range(1, DAYS + 1):
        value = float(input(f"  Day {day}: "))
        daily.append(value)
    expenses[category] = daily
    print()

total_per_category = {
    category: sum(values)
    for category, values in expenses.items()
}

daily_averages = {
    category: total / DAYS
    for category, total in total_per_category.items()
}

weekly_total = sum(total_per_category.values())

highest_category = max(
    total_per_category,
    key=total_per_category.get
)

if weekly_total > WEEKLY_BUDGET_LIMIT:
    print("Weekly budget exceeded!")
    print(f"Spent: {weekly_total:.2f}, Limit: {WEEKLY_BUDGET_LIMIT:.2f}\n")

print("Weekly summary:")
for category in CATEGORIES:
    print(
        f"{category}: "
        f"Total = {total_per_category[category]:.2f}, "
        f"Daily Avg = {daily_averages[category]:.2f}")

print(f"\nHighest spending category: {highest_category}\n")
with open("expense_summary.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Category", "Weekly Total", "Daily Average"])
    for category in CATEGORIES:
        writer.writerow([
            category,
            total_per_category[category],
            daily_averages[category]
        ])

plt.figure() # bar chart 
plt.bar(
    total_per_category.keys(),
    total_per_category.values()
)
plt.title("Weekly Expenses by Category")
plt.ylabel("Amount")
plt.xlabel("Category")
plt.tight_layout()
plt.show()

plt.figure() # pie chart
plt.pie(
    total_per_category.values(),
    labels=total_per_category.keys(),
    autopct="%1.1f%%" # 32.456% will be depicted as 32.5%
)
plt.title("Expense Distribution")
plt.tight_layout()
plt.show()