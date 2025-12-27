import csv
import matplotlib.pyplot as plt


# Category: [[day, expense]]
expenses = {
    "Food": [],
    "Transport": [],
    "Clothes": [],
    "Entertainment": []
}

WEEKLY_BUDGET_LIMIT = 5000

def main() -> None:

    # Test data
    expenses["Food"].append([1, 30])
    expenses["Food"].append([2, 40])
    expenses["Transport"].append([3, 50])

    # Main functions 
    add_expense()
    total_count()
    highest_expenses()
    show_bar_chart()
    calculate_daily_averages()
    show_pie_chart()
    limit()


def add_expense() -> None:
    # User input
    user_category = input().strip()
    day = int(input())
    expense = int(input())

    # Add data
    expenses[user_category].append([day, expense])
    

def total_count() -> None:

    # Sum of each category 
    food_total = sum(item[1] for item in expenses["Food"])
    transport_total = sum(item[1] for item in expenses["Transport"])
    cloth_total = sum(item[1] for item in expenses["Clothes"])
    entertainment_total = sum(item[1] for item in expenses["Entertainment"])

    # Output
    print("Food",food_total)
    print("Transport",transport_total)
    print("Clothes",cloth_total)
    print("Entertainment",entertainment_total)

def highest_expenses() -> None:
    
    # Sum of each category 
    food_total = sum(item[1] for item in expenses["Food"])
    transport_total = sum(item[1] for item in expenses["Transport"])
    cloth_total = sum(item[1] for item in expenses["Clothes"])
    entertainment_total = sum(item[1] for item in expenses["Entertainment"])


    # Store in dictionary to get max category and max expense 
    totals = {
        "Food": food_total,
        "Transport": transport_total,
        "Clothes": cloth_total,
        "Entertainment": entertainment_total
    }

    #Output
    highest_category = max(totals, key=totals.get)
    print(f"Highest expense: {highest_category} = {totals[highest_category]}")

def export_csv() -> None:
    
    # Open csv file
    with open("data.csv", mode="w", newline="", encoding="utf-8") as file:
        writer = csv.file(file)

        writer.writerow(["Category", "Day", "Expense"])

        # Exctract category
        for category, items in expenses.items():
            
            # Extract day and amount
            for day, amount in items:
                writer.writerow([category, day, amount])

    print("Succesful extract")

def show_bar_chart() -> None:
    # Sum of each category 
    food_total = sum(item[1] for item in expenses["Food"])
    transport_total = sum(item[1] for item in expenses["Transport"])
    cloth_total = sum(item[1] for item in expenses["Clothes"])
    entertainment_total = sum(item[1] for item in expenses["Entertainment"])

    # Store in dictionary to get max category and max expense 
    totals = {
        "Food": food_total,
        "Transport": transport_total,
        "Clothes": cloth_total,
        "Entertainment": entertainment_total
    }
    
    categories = list(totals.keys())
    values = list(totals.values())

    # Show bar chart 
    plt.figure(figsize=(8, 5))
    plt.bar(categories, values)
    plt.title("Expenses by Category")
    plt.xlabel("Category")
    plt.ylabel("Total Expense")
    plt.grid(axis="y", linestyle="--", alpha=0.6)
    plt.show()

def calculate_daily_averages() -> None:
    averages = {}

    for category, items in expenses.items():
        total = sum(amount for _, amount in items)
        days = len(items)
        averages[category] = total / days if days > 0 else 0
    
    print(averages)

def show_pie_chart() -> None:
    # Sum of each category 
    food_total = sum(item[1] for item in expenses["Food"])
    transport_total = sum(item[1] for item in expenses["Transport"])
    cloth_total = sum(item[1] for item in expenses["Clothes"])
    entertainment_total = sum(item[1] for item in expenses["Entertainment"])

    # Store in dictionary to get max category and max expense 
    totals = {
        "Food": food_total,
        "Transport": transport_total,
        "Clothes": cloth_total,
        "Entertainment": entertainment_total
    }
    
    labels = totals.keys()
    values = totals.values()

    # Show pie chart
    plt.figure(figsize=(7, 7))
    plt.pie(
        values,
        labels=labels,
        autopct="%1.1f%%",
        startangle=90
    )
    plt.title("Expense Distribution by Category")
    plt.axis("equal")  
    plt.show()

def limit() -> None:

    total = 0

    # Get Sum
    for category in expenses:
        total += sum(item[1] for item in expenses[category])

    # Compare
    if total > WEEKLY_BUDGET_LIMIT:
        print("Limit  Exceeded!")
    else:   
        print("Budget OK")

if __name__ == "__main__":
    main()