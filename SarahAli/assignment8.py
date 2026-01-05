import csv
import matplotlib.pyplot as plt
import os  # To handle file paths


# Step 1: Define categories

categories = ["Food", "Transport", "Clothes", "Entertainment"]
expenses = {}  # dictionary to store daily expenses


# Step 2: Get user input for 7 days

for cat in categories:
    expenses[cat] = []
    print(f"\nEnter expenses for {cat} (7 days):")
    for day in range(1, 8):
        while True:
            try:
                value = float(input(f"  Day {day}: "))
                if value < 0:
                    print("    Expense cannot be negative!")
                    continue
                expenses[cat].append(value)
                break
            except ValueError:
                print("    Please enter a number.")


# Step 3: Calculate totals and averages

total_expenses = {}
average_expenses = {}
for cat in categories:
    total = sum(expenses[cat])
    avg = total / 7
    total_expenses[cat] = total
    average_expenses[cat] = avg


# Step 4: Print summary

print("\nWeekly Expense Summary:")
for cat in categories:
    print(f" {cat}: Total = {total_expenses[cat]:.2f}, Daily Average = {average_expenses[cat]:.2f}")


# Step 5: Find category with highest expense

max_cat = max(total_expenses, key=total_expenses.get)
print(f"\nHighest spending category: {max_cat} ({total_expenses[max_cat]:.2f})")


# Step 6: Save summary to CSV inside the same folder

# Get the folder of the current script
folder = os.path.dirname(os.path.abspath(__file__))
csv_file = os.path.join(folder, "weekly_expenses.csv")

with open(csv_file, "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Category ",  "Total Expense ",  "Daily Average "])
    for cat in categories:
        writer.writerow([cat, total_expenses[cat],  average_expenses[cat]])
print(f"\nSummary saved to '{csv_file}'")


# Step 7: Visualize with bar chart

plt.bar(categories, [total_expenses[cat] for cat in categories], color="skyblue")
plt.title("Weekly Expenses by Category")
plt.ylabel("Total Expense")
plt.show()


# Step 8: Visualize with pie chart

plt.pie([average_expenses[cat] for cat in categories], labels=categories, autopct="%1.1f%%")
plt.title("Daily Average Expenses by Category")
plt.show()


# Step 9: Weekly budget check

while True:
    try:
        budget = float(input("\nEnter your weekly budget limit: "))
        if budget < 0:
            print("Budget cannot be negative!")
            continue
        break
    except ValueError:
        print("Please enter a number.")

total_spent = sum(total_expenses.values())
print(f"Total spent this week: {total_spent:.2f}")

if total_spent > budget:
    print("Warning: You have exceeded your budget!")
else:
    print("You are within your budget.")
