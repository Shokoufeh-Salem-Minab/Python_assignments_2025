from enum import Enum
from dataclasses import dataclass
import matplotlib.pyplot as pyplot


class Category(Enum):
    FOOD = "F"
    TRANSPORT = "T"
    CLOTHES = "C"
    ENTERTAINMENT = "E"


@dataclass
class Expense:
    category: Category
    money: int  # number of cents
    label: str


def load_data(s: str) -> list[Expense]:
    lines = s.splitlines()
    assert len(lines) >= 1, "must have a header line"

    result: list[Expense] = []

    for line in lines[1:]:
        if line == "":
            continue
        parts = line.split(",")
        assert len(parts) == 3, "must have 3 values per line"

        category = Category(parts[0])
        assert category in Category, "must be a valid category"

        label = parts[1]

        assert label != "", "label must be non empty"

        money_f = float(parts[2])
        money = int(money_f * 100)
        assert money > 0, "money must be positive"

        result.append(Expense(category, money, label))

    return result


def money_string(money: int) -> str:
    return f"{money // 100}.{money % 100 :02} EUR"


def csv_string(data) -> str:
    acc = ""
    for line in data:
        acc += ",".join(map(str, line)) + "\n"
    return acc


def main() -> None:
    # Load data from an example file
    with open("weekly_expenses.csv", "tr", encoding="utf8") as f:
        data = load_data(f.read())

    # Calculate total expense per category

    total: dict[Expense, int] = {}
    for val in data:
        if val.category not in total:
            total[val.category] = 0
        total[val.category] += val.money

    print("Totals per category:")
    print(f"Food: {money_string(total[Category.FOOD])}")
    print(f"Transport: {money_string(total[Category.TRANSPORT])}")
    print(f"Clothes: {money_string(total[Category.CLOTHES])}")
    print(f"Entertainment: {money_string(total[Category.ENTERTAINMENT])}")

    # Find category with highest expense

    a = max(total.items(), key=lambda t: t[1])
    print(f"Category with max expense ({money_string(a[1])}): {a[0]}")

    # Save summarized data into a CSV file
    csv_data = csv_string(
        [
            ["name", "value"],
            ["total_f", total[Category.FOOD]],
            ["total_t", total[Category.TRANSPORT]],
            ["total_c", total[Category.CLOTHES]],
            ["total_e", total[Category.ENTERTAINMENT]],
            ["max_name", a[0].value],
            ["max_value", a[1]],
        ]
    )

    with open("summary.csv", "wt", encoding="utf8") as f:
        f.write(csv_data)
        print("Created summary.csv")

    # Bar chart visualization
    pyplot.bar(
        ["Food", "Transport", "Clothes", "Entertainment"],
        [
            total[Category.FOOD] / 100,
            total[Category.TRANSPORT] / 100,
            total[Category.CLOTHES] / 100,
            total[Category.ENTERTAINMENT] / 100,
        ],
    )

    pyplot.savefig("barchart.svg", format="svg")
    pyplot.close()

    # User input for daily expenses

    daily_sum = []
    daily_count = []
    weekly_sum = []

    WEEKLY_WARNING = 20000

    print("Asking user for their daily expenses...")
    print("Input format: <day> <amount>")
    print(
        "<day> is an integer with 0 meaning today, 1 meaning tommorow and so on (example 15)"
    )
    print("<amount> is the amount paid (example: 12.34)")
    print("type exit to exit")
    while True:
        inp = input("> ").strip()
        if inp.lower() == "exit":
            break

        parts = inp.split(" ")
        assert len(parts) == 2, "invalid user input"

        day = int(parts[0])
        amount = int(float(parts[1]) * 100)

        assert day >= 0
        assert amount > 0

        week = day // 7

        while len(daily_count) <= day:
            daily_count.append(0)
        while len(daily_sum) <= day:
            daily_sum.append(0)
        while len(weekly_sum) <= week:
            weekly_sum.append(0)

        daily_count[day] += 1
        daily_sum[day] += amount
        weekly_sum[week] += amount

        if weekly_sum[week] > WEEKLY_WARNING:
            print(
                f"Exceeded weekly limit of {money_string(WEEKLY_WARNING)}:\n"
                f"Week #{week} (days #{week * 7} - #{week * 7 + 6}) has total amount of {money_string(weekly_sum[week])}"
            )

    print("Daily averages:")

    for day in range(len(daily_sum)):
        if daily_count[day] != 0:
            print(f"Day {day}: {money_string(daily_sum[day] // daily_count[day])}")

    data = list(
        filter(lambda x: x[1] != 0, enumerate(map(lambda x: x / 100, daily_sum)))
    )

    # Bar chart visualization
    pyplot.figure()
    pyplot.plot(
        list(map(lambda x: x[0], data)),
        list(map(lambda x: x[1], data)),
        marker="o",
        linestyle="-",
    )
    pyplot.title("Spending per day")
    pyplot.xlabel("Day")
    pyplot.ylabel("Spending (EUR)")
    pyplot.grid(True)
    pyplot.savefig("daily.svg", format="svg")
    pyplot.close()

    # Pie visualization
    pyplot.figure()
    pyplot.plot(
        list(map(lambda x: x[0], data)),
        list(map(lambda x: x[1], data)),
        marker="o",
        linestyle="-",
    )
    pyplot.title("Spending per day")
    pyplot.xlabel("Day")
    pyplot.ylabel("Spending (EUR)")
    pyplot.grid(True)
    pyplot.savefig("daily.svg", format="svg")
    pyplot.close()

    pyplot.pie(
        list(map(lambda x: x[1], data)),
        labels=list(map(lambda x: f"Day {x[0]}", data)),
    )
    pyplot.title("Expenses per day")
    pyplot.savefig("pie.svg", format="svg")
    pyplot.close()


if __name__ == "__main__":
    main()
