#python script for PyBank problem

import os
import csv

csvpath = os.path.join('Resources', 'budget_data.csv')

# def profitTest(budget_data):
#     total_profit = int(budget_data[1])
#     #print(total_profit)

with open(csvpath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    # Read the header row first (skip this step if there is now header)
    csv_header = next(csvreader)

    # initialize number of months and total profit
    number_of_months = 0
    total_profit = 0

    
    # Read each row of data after the header
    for row in csvreader:
        number_of_months += 1
        total_profit += int(row[1])
        #print(f"{row}")
    
    print(number_of_months)
    print(total_profit)
    

