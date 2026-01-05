import csv
import matplotlib.pyplot as plt

# function for calculating total spent
def calc_totals(expenses):
    totals = {}
    for category, values in expenses.items():
        totals[category] = sum(values)
    return totals

weekly_expenses = {}

# user input
for category in ["Food", "Clothes", "Transport", "Entertainment"]:
    print(f"Enter expenses for {category}:")
    daily = []
    for day in range(1, 8):
        daily.append(float(input(f"Day {day}: ")))
    weekly_expenses[category] = daily

# totals and avarage
totals = calc_totals(weekly_expenses)
print("Total Values: ", totals)

print("\nDaily averages:")
for category, values in weekly_expenses.items():
    average = sum(values) / len(values)
    print(f"{category}: {average:.2f} per day")

# budget input
budget = float(input("\nEnter weekly budget limit: "))
total_spent = sum(totals.values())

if total_spent > budget:
    print("WARNING: Weekly budget exceeded!")
else:
    print("You are within the weekly budget.")

# highest spent
highest_category = max(totals, key = totals.get)
print(f"Highest expense category: {highest_category} (${totals[highest_category]})")

# csv file input
with open("weekly_expenses_summary.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Category", "Total Expense"])
    for category, total in totals.items():
        writer.writerow([category, total])

# graphs
categories = list(totals.keys())
amounts = list(totals.values())

# bar chart
plt.figure(figsize=(6, 4))
plt.bar(categories, amounts)
plt.xlabel("Expense Category")
plt.ylabel("total Weekly Expense ($)")
plt.title("Weelky Expense Analysis")
plt.show()

#pie chart
plt.figure(figsize=(6, 6))
plt.pie(
    amounts,
    labels=categories,
    autopct='%1.1f%%',
    startangle=90
)
plt.title("Weekly Expense Distribution")
plt.show()
