import pandas as pd
import matplotlib.pyplot as plt

# get user input for expenses
def get_expenses():
    categories = ['food', 'transport', 'clothes', 'entertainment']
    expenses = {}
    print("-- enter daily expenses for the week --\n")
    for cat in categories:
        print(f"{cat.upper()}")
        expenses[cat] = [float(input(f"  day {i}: $")) for i in range(1, 8)]
    return expenses

# main
print("=" * 50)
print("expense tracker")
print("=" * 50)

# sample data or manual input
if input("\nuse sample data? (y/n): ").lower() == 'y':
    expenses = {
        'food': [45.50, 32.00, 58.20, 41.80, 55.00, 62.30, 48.90],
        'transport': [15.00, 15.00, 20.00, 15.00, 25.00, 18.00, 15.00],
        'clothes': [0.00, 85.00, 0.00, 120.00, 0.00, 45.00, 0.00],
        'entertainment': [25.00, 0.00, 40.00, 35.00, 50.00, 0.00, 30.00]
    }
else:
    expenses = get_expenses()

# create dataframe
df = pd.DataFrame(expenses, index=[f'day{i}' for i in range(1, 8)])

print("\n-- expense dataframe --\n")
print(df)

# calculate totals and averages
totals = df.sum()
averages = df.mean()

print("\n-- summary --\n")
print("totals:", totals.to_dict())
print("averages:", averages.to_dict())
print(f"\nhighest category: {totals.idxmax().upper()} (${totals.max():.2f})")

# save to csv
df_with_total = df.copy()
df_with_total.loc['total'] = totals
df_with_total.to_csv('expenses.csv')
print("\ndata saved to expenses.csv")

# create bar chart
plt.figure(figsize=(10, 5))
totals.plot(kind='bar', color=['#ff6b6b', '#4ecdc4', '#45b7d1', '#ffd93d'])
plt.title('weekly expenses by category')
plt.ylabel('total ($)')
plt.xticks(rotation=45)
for i, v in enumerate(totals):
    plt.text(i, v + 5, f'${v:.2f}', ha='center')
plt.tight_layout()
plt.savefig('expenses_bar_chart.png')
print("bar chart saved")

# create pie chart
plt.figure(figsize=(8, 8))
totals.plot(kind='pie', autopct='%1.1f%%', colors=['#ff6b6b', '#4ecdc4', '#45b7d1', '#ffd93d'])
plt.title('expense distribution')
plt.ylabel('')
plt.tight_layout()
plt.savefig('expenses_pie_chart.png')
print("pie chart saved")

# budget check
budget = float(input("\nenter weekly budget: $"))
total = totals.sum()
print(f"\ntotal spent: ${total:.2f}")
print(f"budget limit: ${budget:.2f}")

if total > budget:
    print(f"warning: over budget by ${total - budget:.2f}!")
else:
    print(f"good job! ${budget - total:.2f} remaining")
