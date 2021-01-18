#python script for PyBank problem

import os
import csv

csvpath = os.path.join('Resources', 'budget_data.csv')

# def data_calcs():
    
#     #total profits
#     profits = []
#     profits.append(int(datafile[1]))
#     total_profits = sum(profits)
#     print(total_profits)


with open(csvpath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    # Read the header row first (skip this step if there is now header)
    csv_header = next(csvreader)

    # initialize variables
    data_list = []
    months_list = []
    profits_list = []
    total_profits = 0
    
    # Read each row of data after the header
    for row in csvreader:

        data_list.append(row)

        # creat months list
        months_list.append(row[0])
        
        # create profit list
        profits_list.append(int(row[1]))

    #print(data_list)
    
    # calculate the total number of months
    total_months = len(months_list)
    # months = []
    # for _ in data_list:
    #     months.append(data_list[0])
    # total_months = len(months)

    # calculate the total profits
    total_profits = sum(profits_list)
    # profits = []
    # for _ in data_list:
    #     profits.append(int(data_list[1]))
    # total_profits = sum(profits)

    #calculate the average change in profits
    change_in_profit = []
    new_months_list = []       
    
    for i in range(len(profits_list) - 1):
        next_value = profits_list[i + 1]
        current_value = profits_list[i]
        change_in_profit.append(next_value - current_value)
        new_months_list.append(months_list[i + 1])

    average_change = sum(change_in_profit) / len(change_in_profit)
    
    # calculate the greatest increase in profit and the month it occured
    greatest_increase = max(change_in_profit)

    # calculate the greatest decrease in profit and the month it occured
    greatest_decrease = min(change_in_profit)
    
    # find date of greatest increase and decrease in profits

    # create dictionary of date:change in profit pairs
    test_dict = dict(zip(new_months_list, change_in_profit))
    
    # search for months based on greatest increase and decrease criteria
    for key in test_dict:
        if test_dict[key] == greatest_increase:
            month_of_greatest_increase = key
        elif test_dict[key] == greatest_decrease:
            month_of_greatest_decrease = key
        

    # print finanical analysis
    print("Financial Analysis")
    print("------------------------------")
    print(f"Total Months: {total_months}")
    print(f"Total Profit: ${total_profits}")
    print(f"Average Change: ${average_change}")
    print(f"Greatest Increase In Profits: {month_of_greatest_increase} (${greatest_increase})")
    print(f"Greatest Decrease In Profits: {month_of_greatest_decrease} (${greatest_decrease})")
    

