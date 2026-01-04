# Jānis Sniedze
# js23127
# Homework 8
# Final edit date: 30/12/2025


import csv  # csv used to write the expense summary file
import os  # os used to build file paths and determine script directory
from typing import Dict, List  # typing annotations for clarity

def defaultExpenses() -> Dict[str, List[float]]:  # return a simple default dataset mapping categories to 7 daily values
	return {
		"Food": [12.5, 9.3, 14.0, 10.2, 11.0, 8.5, 13.0],  # typical daily food expenses for a week
		"Transport": [5.0, 7.2, 4.5, 6.0, 5.5, 4.0, 6.5],  # transport expenses across seven days
		"Clothes": [0.0, 20.0, 0.0, 0.0, 15.0, 0.0, 0.0],  # occasional clothing purchases
		"Entertainment": [8.0, 0.0, 5.0, 12.0, 7.5, 6.0, 0.0],  # entertainment expenses by day
	}


def parseSevenValues(s: str) -> List[float]:  # parse a string into exactly seven float values, supporting commas or whitespace
	sep = "," if "," in s else None  # prefer comma splitting when a comma is present to support comma lists
	parts = [p.strip() for p in s.split(sep)] if sep else s.split()  # split and trim pieces
	values: List[float] = []  # collect parsed numeric values
	for part in parts:
		if part == "":
			continue  # skip empty tokens produced by extra separators
		try:
			values.append(float(part))  # convert token to float and store
		except ValueError:
			raise ValueError(f"Could not parse '{part}' as a number")  # bubble up parse errors with helpful message
	if len(values) != 7:
		raise ValueError("Please provide exactly 7 numbers (one per day)")  # require exactly seven daily values
	return values


def promptUserData(categories: List[str]) -> Dict[str, List[float]]:  # interactively ask user for 7-day values per category
	print("Entering interactive mode: provide expenses for 7 days per category.")  # prompt user about interactive entry
	print("You can enter 7 numbers separated by spaces or commas (e.g. 1 2 3 4 5 6 7")  # example input format
	data: Dict[str, List[float]] = {}  # accumulate results per category
	for cat in categories:
		while True:
			s = input(f"Enter 7 daily expenses for {cat} (or leave empty to use zeros): ")  # read user input line
			if s.strip() == "":
				data[cat] = [0.0] * 7  # default to zeros when user leaves input blank
				break
			try:
				vals = parseSevenValues(s)  # try parsing the provided line into seven floats
				data[cat] = vals
				break
			except ValueError as e:
				print("Input error:", e)  # show parse error to the user
				print("Try again.")  # prompt to re-enter
	return data


def summarize(expenses: Dict[str, List[float]]):  # compute totals per category, averages, and daily totals across categories
	totals = {cat: sum(days) for cat, days in expenses.items()}  # total spent per category for the week
	averages = {cat: (totals[cat] / 7) for cat in totals}  # average per day per category (7 days assumed)
	dailyTotals = [sum(expenses[cat][i] for cat in expenses) for i in range(7)]  # sum across categories for each day
	return totals, averages, dailyTotals


def saveCsv(expenses: Dict[str, List[float]], totals: Dict[str, float], averages: Dict[str, float], outPath: str):  # write CSV summary with header and rounded totals/averages
	header = ["Category"] + [f"Day{i+1}" for i in range(7)] + ["Total", "Average"]  # CSV header with day columns
	with open(outPath, "w", newline="", encoding="utf-8") as fh:
		writer = csv.writer(fh)  # create csv writer
		writer.writerow(header)  # write header row first
		for cat, days in expenses.items():
			writer.writerow([cat] + days + [round(totals[cat], 2), round(averages[cat], 2)])  # write each category row with rounded totals


def makeCharts(totals: Dict[str, float], outputDir: str, show: bool = False):  # create bar and pie charts and save to files
	import matplotlib  # import matplotlib locally to avoid hard dependency when not plotting
	if not show:
		matplotlib.use("Agg")  # use non-interactive backend when not showing charts
	import matplotlib.pyplot as plt  # pyplot for plotting operations

	categoriesList = list(totals.keys())  # ordered list of category names for plotting
	valuesList = [totals[c] for c in categoriesList]  # corresponding numeric totals

	# generate bar chart showing totals per category
	plt.figure(figsize=(8, 5))
	bars = plt.bar(categoriesList, valuesList, color=["#4c72b0", "#55a868", "#c44e52", "#8172b2"])  # draw bars with consistent colors
	plt.title("Weekly Expenses by Category")
	plt.ylabel("Amount")
	plt.grid(axis="y", linestyle="--", alpha=0.3)
	for bar, val in zip(bars, valuesList):
		plt.text(bar.get_x() + bar.get_width() / 2, val + 0.5, f"{val:.2f}", ha="center")  # annotate each bar with its value
	barPath = os.path.join(outputDir, "expenses_bar.png")  # file path for saved bar chart
	plt.tight_layout()
	plt.savefig(barPath)  # save chart image to disk
	if show:
		plt.show()  # optionally display chart to user when requested
	plt.close()

	# generate pie chart showing distribution across categories
	plt.figure(figsize=(6, 6))
	plt.pie(valuesList, labels=categoriesList, autopct="%.1f%%", startangle=140, colors=["#4c72b0", "#55a868", "#c44e52", "#8172b2"])  # pie with label and percent
	plt.title("Expense Distribution")
	piePath = os.path.join(outputDir, "expenses_pie.png")  # file path for pie chart
	plt.savefig(piePath)  # save pie chart image
	if show:
		plt.show()  # optionally display pie chart
	plt.close()

	return barPath, piePath


def main():  # main entry: use defaults unless interactive mode is enabled manually in this code
	interactive = False  # default not to prompt; set True to prompt interactively
	budget = 200.0  # weekly budget used to warn when exceeded
	showCharts = False  # whether charts should be shown interactively

	categories = ["Food", "Transport", "Clothes", "Entertainment"]  # categories considered in the tracker

	if interactive:
		expenses = promptUserData(categories)  # ask user for values when interactive
	else:
		expenses = defaultExpenses()  # otherwise use small default dataset for demo

	totals, averages, dailyTotals = summarize(expenses)  # compute aggregate summaries

	# pick the category with largest total spending
	highest = max(totals, key=totals.get)  # find key with maximum value in totals

	# prepare output paths next to this script for convenience
	outDir = os.path.dirname(os.path.abspath(__file__))  # directory where this script resides
	csvPath = os.path.join(outDir, "expenses_summary.csv")  # CSV output file path

	saveCsv(expenses, totals, averages, csvPath)  # write CSV summary to disk

	# generate charts and optionally display them
	barPath, piePath = makeCharts(totals, outDir, show=showCharts)

	totalWeek = sum(totals.values())  # total expenditure across all categories for the week

	# display a concise summary to the user
	print("Weekly expense summary:")
	for cat in categories:
		print(f" - {cat}: total={totals[cat]:.2f}, avg/day={averages[cat]:.2f}")
	print(f"Category with highest total: {highest} ({totals[highest]:.2f})")
	print(f"Total for week: {totalWeek:.2f}")
	print(f"Daily totals: {', '.join(f'{d:.2f}' for d in dailyTotals)}")
	print(f"CSV saved to: {csvPath}")
	print(f"Bar chart saved to: {barPath}")
	print(f"Pie chart saved to: {piePath}")

	if totalWeek > budget:
		print("WARNING: Weekly budget exceeded! Limit:", budget)  # warn when spending exceeds budget
	else:
		print("Within weekly budget.")  # otherwise indicate spending is within budget


if __name__ == "__main__":
	main()

