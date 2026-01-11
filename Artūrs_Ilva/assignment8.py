weekly_expenses = {
    "Food": [12, 15, 10, 20, 13, 18, 17],
    "Transport": [5, 6, 5, 7, 5, 6, 5],
    "Clothes": [0, 0, 0, 30, 0, 0, 0],
    "Entertainment": [10, 0, 15, 0, 10, 5, 0]
}

def calculate_totals(expenses):
    totals = {}
    for category, values in expenses.items():
        totals[category] = sum(values)
    return totals

totals = calculate_totals(weekly_expenses)
print(totals)

highest_category = max(totals, key=totals.get)
print(f"Highest expense category: {highest_category} (${totals[highest_category]})")

import csv

with open("weekly_expense_summary.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Category", "Total Expense"])
    for category, total in totals.items():
        writer.writerow([category, total])

import matplotlib.pyplot as plt

categories = list(totals.keys())
amounts = list(totals.values())

plt.figure(figsize=(6, 4))
plt.bar(categories, amounts)
plt.xlabel("Expense Category")
plt.ylabel("Total Weekly Expense ($)")
plt.title("Weekly Expense Analysis")
plt.show()

use_input = input("Do you want to enter your own daily expenses? (yes/no): ").strip().lower()
if use_input == "yes":
    weekly_expenses = {
        "Food": [],
        "Transport": [],
        "Clothes": [],
        "Entertainment": []
    }
    for day in range(1, 8):
        print(f"\nDay {day} expenses:")
        for category in weekly_expenses:
            value = float(input(f"  Enter {category} expense: "))
            weekly_expenses[category].append(value)
    totals = calculate_totals(weekly_expenses)
    print("\nUpdated totals:", totals)
    highest_category = max(totals, key=totals.get)
    print(f"Highest expense category: {highest_category} (${totals[highest_category]})")
    with open("weekly_expense_summary.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Category", "Total Expense"])
        for category, total in totals.items():
            writer.writerow([category, total])

daily_averages = {}
for category, values in weekly_expenses.items():
    daily_averages[category] = sum(values) / len(values)
print("\nDaily averages:", daily_averages)

categories = list(totals.keys())
amounts = list(totals.values())
plt.figure(figsize=(6, 6))
plt.pie(amounts, labels=categories, autopct="%1.1f%%")
plt.title("Weekly Expenses Breakdown")
plt.show()

budget_limit = float(input("\nSet your weekly budget limit: "))
total_spent = sum(totals.values())
print(f"Total spent this week: ${total_spent}")

if total_spent > budget_limit:
    print("You exceeded your weekly budget!")
else:
    print("You are within your weekly budget!")
