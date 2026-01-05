import csv
import matplotlib.pyplot as plt


categories = ["Food", "Transport", "Clothes", "Entertainment"]
days = 7


WEEKLY_BUDGET = 300


expenses = {}


for category in categories:
    print(f"\nEnter expenses for {category} (7 days):")
    daily = []
    for day in range(1, days + 1):
        amount = float(input(f"  Day {day}: "))
        daily.append(amount)
    expenses[category] = daily


total_per_category = {cat: sum(vals) for cat, vals in expenses.items()}
daily_averages = {cat: total / days for cat, total in total_per_category.items()}
highest_category = max(total_per_category, key=total_per_category.get)
overall_total = sum(total_per_category.values())


if overall_total > WEEKLY_BUDGET:
    print("\n⚠️ WARNING: Weekly budget exceeded!")
else:
    print("\n✅ Weekly budget is within limit.")


print("\nExpense Summary:")
for cat in categories:
    print(f"{cat}: Total = {total_per_category[cat]}, Average per day = {daily_averages[cat]:.2f}")

print(f"\nHighest expense category: {highest_category}")


with open("weekly_expenses_summary.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Category", "Total Expense", "Daily Average"])
    for cat in categories:
        writer.writerow([cat, total_per_category[cat], round(daily_averages[cat], 2)])

print("\nData saved to weekly_expenses_summary.csv")

plt.figure()
plt.bar(total_per_category.keys(), total_per_category.values())
plt.title("Weekly Expenses by Category")
plt.xlabel("Category")
plt.ylabel("Total Expense")
plt.show()


plt.figure()
plt.pie(
    total_per_category.values(),
    labels=total_per_category.keys(),
    autopct="%1.1f%%"
)
plt.title("Expense Distribution")
plt.show()
