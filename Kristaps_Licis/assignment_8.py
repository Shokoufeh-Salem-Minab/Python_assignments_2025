import csv
import matplotlib.pyplot as plt
from datetime import datetime


def get_user_expenses():
    """Get daily expenses from user input for all categories."""
    categories = ['Food', 'Transport', 'Clothes', 'Entertainment']
    expenses = {}
    days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    
    print("\n" + "="*70)
    print("ENTER DAILY EXPENSES FOR THE WEEK")
    print("="*70)
    
    for category in categories:
        print(f"\n{category}:")
        category_expenses = []
        
        for day in days:
            while True:
                try:
                    expense = float(input(f"  {day}: €"))
                    if expense < 0:
                        print("    Please enter a positive number.")
                        continue
                    category_expenses.append(expense)
                    break
                except ValueError:
                    print("    Invalid input. Please enter a number.")
        
        expenses[category] = category_expenses
    
    return expenses


def use_sample_data():
    """Return sample expense data for demonstration."""
    return {
        'Food': [12.50, 15.30, 10.80, 18.20, 14.60, 22.40, 16.90],
        'Transport': [5.00, 5.00, 5.00, 5.00, 5.00, 8.50, 0.00],
        'Clothes': [0.00, 0.00, 45.00, 0.00, 0.00, 30.00, 0.00],
        'Entertainment': [8.00, 0.00, 12.50, 15.00, 20.00, 25.00, 18.00]
    }


def calculate_totals(expenses):
    """Calculate total expense for each category."""
    totals = {}
    for category, daily_expenses in expenses.items():
        totals[category] = sum(daily_expenses)
    return totals


def calculate_daily_averages(expenses):
    """Calculate daily average for each category."""
    averages = {}
    for category, daily_expenses in expenses.items():
        averages[category] = sum(daily_expenses) / len(daily_expenses)
    return averages


def find_highest_category(totals):
    """Find the category with highest total expense."""
    return max(totals, key=totals.get)


def save_to_csv(expenses, totals, averages, filename="expenses_summary.csv"):
    """Save expense data to CSV file."""
    with open(filename, 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        
        # Header
        writer.writerow(['Generated', datetime.now().strftime('%Y-%m-%d %H:%M:%S')])
        writer.writerow([])
        
        # Daily expenses
        writer.writerow(['Category', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun', 'Total', 'Average'])
        
        for category in expenses.keys():
            row = [category] + expenses[category] + [totals[category], f"{averages[category]:.2f}"]
            writer.writerow(row)
        
        # Summary
        writer.writerow([])
        writer.writerow(['SUMMARY'])
        writer.writerow(['Total Weekly Expense', sum(totals.values())])
        writer.writerow(['Highest Category', find_highest_category(totals)])
    
    print(f"\nData saved to '{filename}'")


def create_bar_chart(totals):
    """Create and display bar chart of category totals."""
    categories = list(totals.keys())
    values = list(totals.values())
    
    plt.figure(figsize=(10, 6))
    bars = plt.bar(categories, values, color=['#FF6B6B', '#4ECDC4', '#45B7D1', '#FFA07A'])
    
    plt.xlabel('Category', fontsize=12)
    plt.ylabel('Total Expense (€)', fontsize=12)
    plt.title('Weekly Expenses by Category', fontsize=14, fontweight='bold')
    plt.grid(axis='y', alpha=0.3)
    
    # Add value labels on bars
    for bar in bars:
        height = bar.get_height()
        plt.text(bar.get_x() + bar.get_width()/2., height,
                f'€{height:.2f}',
                ha='center', va='bottom', fontsize=10)
    
    plt.tight_layout()
    plt.savefig('expenses_bar_chart.png')
    print("Bar chart saved as 'expenses_bar_chart.png'")
    plt.show()


def create_pie_chart(totals):
    """Create and display pie chart of category distribution."""
    categories = list(totals.keys())
    values = list(totals.values())
    colors = ['#FF6B6B', '#4ECDC4', '#45B7D1', '#FFA07A']
    
    plt.figure(figsize=(10, 8))
    
    # Create pie chart
    wedges, texts, autotexts = plt.pie(values, labels=categories, autopct='%1.1f%%',
                                        colors=colors, startangle=90,
                                        textprops={'fontsize': 11})
    
    # Enhance text
    for autotext in autotexts:
        autotext.set_color('white')
        autotext.set_fontweight('bold')
    
    plt.title('Weekly Expense Distribution', fontsize=14, fontweight='bold')
    
    # Add legend with amounts
    legend_labels = [f'{cat}: €{val:.2f}' for cat, val in zip(categories, values)]
    plt.legend(legend_labels, loc='upper left', bbox_to_anchor=(1, 1))
    
    plt.tight_layout()
    plt.savefig('expenses_pie_chart.png')
    print("Pie chart saved as 'expenses_pie_chart.png'")
    plt.show()


def check_budget(total_expense, budget_limit):
    """Check if total expense exceeds budget and display warning."""
    print("\n" + "="*70)
    print("BUDGET CHECK")
    print("="*70)
    print(f"Weekly Budget Limit: €{budget_limit:.2f}")
    print(f"Total Expense: €{total_expense:.2f}")
    
    remaining = budget_limit - total_expense
    
    if total_expense > budget_limit:
        overspend = total_expense - budget_limit
        print(f"\n[WARNING] Budget exceeded by €{overspend:.2f}!")
        print("You need to reduce your spending!")
    elif remaining < budget_limit * 0.1:  # Less than 10% remaining
        print(f"\n[CAUTION] Only €{remaining:.2f} remaining ({(remaining/budget_limit)*100:.1f}% of budget)")
        print("You're close to your limit!")
    else:
        print(f"\n[OK] Remaining budget: €{remaining:.2f}")
        print("You're within budget!")


def display_summary(expenses, totals, averages):
    """Display detailed summary of expenses."""
    print("\n" + "="*70)
    print("EXPENSE SUMMARY")
    print("="*70)
    
    days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
    
    # Header
    print(f"\n{'Category':<15}", end="")
    for day in days:
        print(f"{day:>8}", end="")
    print(f"{'Total':>10}{'Average':>10}")
    print("-"*70)
    
    # Data rows
    for category, daily_expenses in expenses.items():
        print(f"{category:<15}", end="")
        for expense in daily_expenses:
            print(f"€{expense:>6.2f}", end=" ")
        print(f"€{totals[category]:>8.2f}€{averages[category]:>8.2f}")
    
    # Total row
    print("-"*70)
    total_weekly = sum(totals.values())
    print(f"{'TOTAL':<15}", end="")
    
    # Calculate daily totals
    for day_idx in range(7):
        day_total = sum(expenses[cat][day_idx] for cat in expenses.keys())
        print(f"€{day_total:>6.2f}", end=" ")
    
    print(f"€{total_weekly:>8.2f}")
    print()


def main():
    print("="*70)
    print("WEEKLY EXPENSE TRACKER")
    print("="*70)
    
    # Choose data input method
    print("\nHow would you like to input data?")
    print("1. Enter manually")
    print("2. Use sample data")
    
    choice = input("\nChoice (1 or 2): ").strip()
    
    if choice == '1':
        expenses = get_user_expenses()
    else:
        print("\nUsing sample data...")
        expenses = use_sample_data()
    
    # Calculate statistics
    totals = calculate_totals(expenses)
    averages = calculate_daily_averages(expenses)
    highest_category = find_highest_category(totals)
    total_weekly = sum(totals.values())
    
    # Display summary
    display_summary(expenses, totals, averages)
    
    # Display insights
    print("\n" + "="*70)
    print("INSIGHTS")
    print("="*70)
    print(f"Total Weekly Expense: €{total_weekly:.2f}")
    print(f"Highest Spending Category: {highest_category} (€{totals[highest_category]:.2f})")
    print(f"Daily Average Spending: €{total_weekly/7:.2f}")
    
    # Budget check
    print("\n" + "-"*70)
    budget = float(input("Enter your weekly budget limit (€): "))
    check_budget(total_weekly, budget)
    
    # Save to CSV
    print("\n" + "-"*70)
    save_to_csv(expenses, totals, averages)
    
    # Create visualizations
    print("\n" + "-"*70)
    print("Generating visualizations...")
    create_bar_chart(totals)
    create_pie_chart(totals)
    
    print("\n" + "="*70)
    print("EXPENSE TRACKING COMPLETED!")
    print("="*70)


if __name__ == "__main__":
    main()
