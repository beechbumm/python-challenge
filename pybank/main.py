import csv
import os

file_to_load = os.getcwd()+'/Resources/budget_data.csv'
# Read the CSV file and load the data
financial_data = []
with open(file_to_load, 'r') as file:
    csv_reader = csv.DictReader(file)
    for row in csv_reader:
        financial_data.append({"Date": row["Date"], "Profit/Losses": int(row["Profit/Losses"])})

# Calculate financial metrics
total_months = len(financial_data)
total_profit_losses = sum(data["Profit/Losses"] for data in financial_data)
profit_changes = [financial_data[i+1]["Profit/Losses"] - financial_data[i]["Profit/Losses"] for i in range(total_months-1)]
average_change = round(sum(profit_changes) / (total_months - 1), 2)
greatest_increase = max(profit_changes)
greatest_increase_date = financial_data[profit_changes.index(greatest_increase) + 1]["Date"]
greatest_decrease = min(profit_changes)
greatest_decrease_date = financial_data[profit_changes.index(greatest_decrease) + 1]["Date"]

# Print analysis to terminal
print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${total_profit_losses}")
print(f"Average Change: ${average_change}")
print(f"Greatest Increase in Profits: {greatest_increase_date} (${greatest_increase})")
print(f"Greatest Decrease in Profits: {greatest_decrease_date} (${greatest_decrease})")

# Export results to a text file
output_file = os.getcwd()+'/analysis/financial_analysis.txt'

with open(output_file, 'w') as file:
    file.write("Financial Analysis\n")
    file.write("----------------------------\n")
    file.write(f"Total Months: {total_months}\n")
    file.write(f"Total: ${total_profit_losses}\n")
    file.write(f"Average Change: ${average_change}\n")
    file.write(f"Greatest Increase in Profits: {greatest_increase_date} (${greatest_increase})\n")
    file.write(f"Greatest Decrease in Profits: {greatest_decrease_date} (${greatest_decrease})\n")

print("Financial analysis results have been saved to 'financial_analysis.txt'.")
