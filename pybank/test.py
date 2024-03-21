import csv
import os


file_path = os.getcwd() + "/Resources/budget_data.csv"

csv_data = []

try:
    with open(file_path, "r") as file: 
        data = csv.reader(file)
        for d in data:
            csv_data.append(d)
        
except FileNotFoundError as e:
    print(e)
    
totalMonth = len(csv_data) - 1
totalProfit = 0
for i in range(1, len(csv_data)):
    monthArr = csv_data[i]
    price = int(monthArr[1])
    totalProfit += price
  
prices = [csv_data[price][1] for price in range(1, len(csv_data))]

changesList = [int(prices[i+1])-int(prices[i]) for i in range(len(prices)-1)]
averageChanges = round(sum(changesList) / (totalMonth - 1), 2)

greatestIncrease = 0
for i in range(1, len(csv_data)):
    price = int(csv_data[i][1])
    if price > greatestIncrease:
        greatestIncrease = price

print("From line 36 ",greatestIncrease)


def showData(total_month, total_profit):
    print("Financial Analysis")
    print("----------------------------")
    print(f"Total Months: {total_month}")
    print(f"Total: ${total_profit}")
    print(f"Average Change: ${averageChanges}")
    
    

showData(totalMonth, totalProfit)