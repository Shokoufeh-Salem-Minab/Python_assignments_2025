import csv
import matplotlib.pyplot as plt

# Data structure
expenses = {
    'Food': [],
    'Transport': [],
    'Clothes': [],
    'Entertainment': []
}

# Input function
def input_expenses():
    for category in expenses:
        print(f"\n{category} expenses:")
        for day in range(1, 8):
            while True:
                try:
                    expense = float(input(f"Day {day}: "))
                    if expense >= 0:
                        expenses[category].append(expense)
                        break
                    else:
                        print("Positive values only")
                except ValueError:
                    print("Numbers only")

# Calculate totals
def calculate_totals():
    totals = {}
    for category, daily in expenses.items():
        totals[category] = sum(daily)
    return totals

# Calculate averages
def calculate_averages():
    averages = {}
    for category, daily in expenses.items():
        averages[category] = sum(daily) / len(daily)
    return averages

# Find highest
def find_highest(totals):
    highest_cat = max(totals, key=totals.get)
    highest_val = totals[highest_cat]
    return highest_cat, highest_val

# Budget check
def check_budget(totals, budget):
    total_spent = sum(totals.values())
    if total_spent > budget:
        print(f"\nWARNING: Budget exceeded by {total_spent - budget:.2f}")
    return total_spent

# Save CSV
def save_csv(totals, averages):
    with open('expenses_summary.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Category', 'Total', 'Average'])
        for category in totals:
            writer.writerow([category, totals[category], averages[category]])

# Bar chart
def plot_bar(totals):
    categories = list(totals.keys())
    values = list(totals.values())
    
    plt.figure(figsize=(10, 6))
    plt.bar(categories, values, color=['blue', 'green', 'red', 'purple'])
    plt.title('Weekly Expenses by Category')
    plt.xlabel('Category')
    plt.ylabel('Total Amount')
    plt.tight_layout()
    plt.savefig('expenses_bar.png')
    plt.show()

# Pie chart
def plot_pie(totals):
    plt.figure(figsize=(8, 8))
    plt.pie(totals.values(), labels=totals.keys(), autopct='%1.1f%%')
    plt.title('Expense Distribution')
    plt.tight_layout()
    plt.savefig('expenses_pie.png')
    plt.show()

# Display summary
def display_summary(totals, averages, highest_cat, highest_val, total_spent):
    print("\n" + "="*40)
    print("WEEKLY EXPENSE SUMMARY")
    print("="*40)
    
    for category in totals:
        print(f"{category}:")
        print(f"  Total: ${totals[category]:.2f}")
        print(f"  Daily Avg: ${averages[category]:.2f}")
        print(f"  Daily Expenses: {expenses[category]}")
    
    print(f"\nHighest spending: {highest_cat} (${highest_val:.2f})")
    print(f"Total spent: ${total_spent:.2f}")

# Main function
def main():
    print("Weekly Expense Tracker")
    print("="*40)
    
    # Get budget
    while True:
        try:
            budget = float(input("\nEnter weekly budget: "))
            if budget >= 0:
                break
            else:
                print("Positive budget only")
        except ValueError:
            print("Numbers only")
    
    # Input expenses
    input_expenses()
    
    # Calculations
    totals = calculate_totals()
    averages = calculate_averages()
    highest_cat, highest_val = find_highest(totals)
    total_spent = check_budget(totals, budget)
    
    # Save and visualize
    save_csv(totals, averages)
    display_summary(totals, averages, highest_cat, highest_val, total_spent)
    plot_bar(totals)
    plot_pie(totals)
    
    print("\nData saved to 'expenses_summary.csv'")
    print("Charts saved as 'expenses_bar.png' and 'expenses_pie.png'")

if __name__ == "__main__":
    main()