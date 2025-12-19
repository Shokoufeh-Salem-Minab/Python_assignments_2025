import pandas as pd
import csv
import matplotlib.pyplot as plt

def prompt_week(category):
    values = input(f"Daily expenses for {category} (separate by commas): ")
    values_list = [float(x.strip()) for x in values.split(",") if x.strip().isnumeric()]
    
    # Replace missing values with zeros
    if(len(values_list) < 7):
        zero_values = [0] * (7-len(values_list))
        values_list += zero_values

    # Return last seven nums
    return pd.Series(values_list[:7])

# Initialize the data
weekly_limit = 200
expenses = {
    "Food": prompt_week("Food"),
    "Transport": prompt_week("Transport"),
    "Clothes": prompt_week("Clothes"),
    "Entertainment": prompt_week("Entertainment"),
}

# Calculate totals
totals = {category: values.sum() for category, values in expenses.items()}

# Find and print the highest total
highest_category = max(totals, key=totals.get)
print(f"the highest category is \"{highest_category}\" with the total - {totals[highest_category]}")

# Save totals to csv
with open("assingment8/weekly_expense_summary.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Category","Total Expense"])
    for category, total in totals.items():
        writer.writerow([category,total])

# Calculate averages
averages = {category: values.mean() for category, values in expenses.items()}

# Plot a pie chart
categories = list(totals.keys())
total_values = list(totals.values())
average_values = list(averages.values())

# Bar plot for totals
plt.subplot(2, 1, 1)
plt.bar(categories,total_values)
plt.xlabel("Category")
plt.ylabel("Total Expenses")

# Show a warning
full_expenses = sum(totals.values())
if(full_expenses > 200):
     plt.title( f"Total Expenses\nWarning the weekly budget of {weekly_limit} is exceeded,\ncurrent expenses - {full_expenses}!", color='red')
else:
    plt.title("Total Expenses")

# Pie plot for average expenses
plt.subplot(2, 1, 2)
plt.pie(average_values,labels=categories)
plt.title("Average Expenses")

# Show the plot
plt.tight_layout()
plt.show()