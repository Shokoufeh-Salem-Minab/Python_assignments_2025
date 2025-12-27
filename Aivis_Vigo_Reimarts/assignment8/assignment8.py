"""
Expense Tracker - Homework Solution (Fixed for Local Use)
Python Lecture 15: Data Visualization

Features:
1. User input for daily expenses
2. Calculate daily averages
3. Pie chart visualization
4. Weekly budget limit with warnings
"""

import matplotlib.pyplot as plt
import csv
import os


def get_user_expenses():
    """
    Collects daily expenses from user input for each category.
    Returns a dictionary with categories and their daily expenses.
    """
    categories = ["Food", "Transport", "Clothes", "Entertainment"]
    weekly_expenses = {}
    
    print("=" * 50)
    print("WEEKLY EXPENSE TRACKER")
    print("=" * 50)
    print("\nPlease enter your daily expenses for each category.")
    print("(Enter expenses for 7 days)\n")
    
    for category in categories:
        print(f"\n--- {category} ---")
        daily_expenses = []
        
        for day in range(1, 8):
            while True:
                try:
                    expense = float(input(f"  Day {day}: $"))
                    if expense < 0:
                        print("  Error: Expense cannot be negative. Try again.")
                        continue
                    daily_expenses.append(expense)
                    break
                except ValueError:
                    print("  Error: Please enter a valid number.")
        
        weekly_expenses[category] = daily_expenses
    
    return weekly_expenses


def calculate_totals(expenses):
    """
    Calculate total expenses for each category.
    """
    totals = {}
    for category, values in expenses.items():
        totals[category] = sum(values)
    return totals


def calculate_daily_averages(expenses):
    """
    Calculate daily average expenses for each category.
    """
    averages = {}
    for category, values in expenses.items():
        averages[category] = sum(values) / len(values)
    return averages


def check_budget_limit(totals, budget_limit):
    """
    Check if total expenses exceed the weekly budget limit.
    Returns True if budget is exceeded, False otherwise.
    """
    total_expenses = sum(totals.values())
    
    print("\n" + "=" * 50)
    print("BUDGET ANALYSIS")
    print("=" * 50)
    print(f"Weekly Budget Limit: ${budget_limit:.2f}")
    print(f"Total Weekly Expenses: ${total_expenses:.2f}")
    
    if total_expenses > budget_limit:
        difference = total_expenses - budget_limit
        print(f"\n⚠️  WARNING: You have EXCEEDED your budget by ${difference:.2f}!")
        print(f"That's {(difference/budget_limit)*100:.1f}% over budget.")
        return True
    else:
        remaining = budget_limit - total_expenses
        print(f"\n✓ Good job! You're within budget.")
        print(f"Remaining budget: ${remaining:.2f}")
        return False


def save_to_csv(totals, averages, filename="expense_summary.csv"):
    """
    Save expense summary to a CSV file in the current directory.
    """
    with open(filename, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Category", "Total Expense", "Daily Average"])
        
        for category in totals.keys():
            writer.writerow([
                category, 
                f"{totals[category]:.2f}", 
                f"{averages[category]:.2f}"
            ])
    
    # Get absolute path for display
    abs_path = os.path.abspath(filename)
    print(f"\n✓ Data saved to: {abs_path}")


def create_bar_chart(totals, filename="expense_bar_chart.png"):
    """
    Create a bar chart showing total expenses by category.
    Saves to current directory.
    """
    categories = list(totals.keys())
    amounts = list(totals.values())
    
    plt.figure(figsize=(10, 6))
    bars = plt.bar(categories, amounts, color=['#FF6B6B', '#4ECDC4', '#45B7D1', '#FFA07A'])
    
    # Add value labels on top of bars
    for bar in bars:
        height = bar.get_height()
        plt.text(bar.get_x() + bar.get_width()/2., height,
                f'${height:.2f}',
                ha='center', va='bottom', fontweight='bold')
    
    plt.xlabel("Expense Category", fontsize=12, fontweight='bold')
    plt.ylabel("Total Weekly Expense ($)", fontsize=12, fontweight='bold')
    plt.title("Weekly Expense Analysis - Bar Chart", fontsize=14, fontweight='bold')
    plt.grid(axis='y', alpha=0.3)
    plt.tight_layout()
    
    # Save to current directory
    plt.savefig(filename, dpi=300, bbox_inches='tight')
    plt.close()
    
    # Get absolute path for display
    abs_path = os.path.abspath(filename)
    print(f"✓ Bar chart saved to: {abs_path}")


def create_pie_chart(totals, filename="expense_pie_chart.png"):
    """
    Create a pie chart showing expense distribution.
    Saves to current directory.
    """
    categories = list(totals.keys())
    amounts = list(totals.values())
    
    # Define colors for each category
    colors = ['#FF6B6B', '#4ECDC4', '#45B7D1', '#FFA07A']
    
    plt.figure(figsize=(10, 8))
    
    # Create pie chart with percentages
    wedges, texts, autotexts = plt.pie(
        amounts, 
        labels=categories, 
        autopct='%1.1f%%',
        startangle=90,
        colors=colors,
        explode=(0.05, 0.05, 0.05, 0.05),  # Slightly separate slices
        shadow=True
    )
    
    # Enhance text properties
    for text in texts:
        text.set_fontsize(12)
        text.set_fontweight('bold')
    
    for autotext in autotexts:
        autotext.set_color('white')
        autotext.set_fontsize(11)
        autotext.set_fontweight('bold')
    
    plt.title("Weekly Expense Distribution - Pie Chart", 
              fontsize=14, fontweight='bold', pad=20)
    
    # Add legend with dollar amounts
    legend_labels = [f'{cat}: ${amt:.2f}' for cat, amt in zip(categories, amounts)]
    plt.legend(legend_labels, loc='upper left', bbox_to_anchor=(1, 1))
    
    plt.tight_layout()
    
    # Save to current directory
    plt.savefig(filename, dpi=300, bbox_inches='tight')
    plt.close()
    
    # Get absolute path for display
    abs_path = os.path.abspath(filename)
    print(f"✓ Pie chart saved to: {abs_path}")


def display_summary(expenses, totals, averages):
    """
    Display a comprehensive summary of expenses.
    """
    print("\n" + "=" * 50)
    print("EXPENSE SUMMARY")
    print("=" * 50)
    
    for category in expenses.keys():
        print(f"\n{category}:")
        print(f"  Daily expenses: {expenses[category]}")
        print(f"  Total: ${totals[category]:.2f}")
        print(f"  Daily average: ${averages[category]:.2f}")
    
    print("\n" + "-" * 50)
    print(f"GRAND TOTAL: ${sum(totals.values()):.2f}")
    print(f"Overall daily average: ${sum(totals.values())/7:.2f}")
    print("-" * 50)
    
    # Find highest expense category
    highest_category = max(totals, key=totals.get)
    print(f"\nHighest expense category: {highest_category} (${totals[highest_category]:.2f})")


def main():
    """
    Main function to run the expense tracker program.
    """
    # Option to use sample data or user input
    print("Welcome to the Weekly Expense Tracker!\n")
    print("1. Enter your own expenses")
    print("2. Use sample data for demonstration")
    
    while True:
        choice = input("\nChoose an option (1 or 2): ").strip()
        if choice in ['1', '2']:
            break
        print("Invalid choice. Please enter 1 or 2.")
    
    if choice == '1':
        # Get user input
        weekly_expenses = get_user_expenses()
    else:
        # Use sample data
        print("\nUsing sample data...")
        weekly_expenses = {
            "Food": [12, 15, 10, 20, 13, 18, 17],
            "Transport": [5, 6, 5, 7, 5, 6, 5],
            "Clothes": [0, 0, 0, 30, 0, 0, 0],
            "Entertainment": [10, 0, 15, 0, 10, 5, 0]
        }
    
    # Get budget limit from user
    while True:
        try:
            budget_limit = float(input("\nEnter your weekly budget limit: $"))
            if budget_limit <= 0:
                print("Budget must be positive. Try again.")
                continue
            break
        except ValueError:
            print("Please enter a valid number.")
    
    # Calculate totals and averages
    totals = calculate_totals(weekly_expenses)
    averages = calculate_daily_averages(weekly_expenses)
    
    # Display summary
    display_summary(weekly_expenses, totals, averages)
    
    # Check budget limit
    check_budget_limit(totals, budget_limit)
    
    # Save to CSV
    save_to_csv(totals, averages)
    
    # Create visualizations
    print("\n" + "=" * 50)
    print("GENERATING VISUALIZATIONS")
    print("=" * 50)
    create_bar_chart(totals)
    create_pie_chart(totals)
    
    print("\n" + "=" * 50)
    print("FILES SAVED SUCCESSFULLY")
    print("=" * 50)
    print(f"\nAll files have been saved to:")
    print(f"  {os.path.abspath('.')}")
    print("\nGenerated files:")
    print("  • expense_summary.csv")
    print("  • expense_bar_chart.png")
    print("  • expense_pie_chart.png")
    
    print("\n" + "=" * 50)
    print("Thank you for using the Expense Tracker!")
    print("=" * 50)


if __name__ == "__main__":
    main()
