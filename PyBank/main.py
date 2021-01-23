#python script for PyBank problem

# import modules
import os
import csv

# file path to data file
csvpath = os.path.join('Resources', 'budget_data.csv')

# open csv file
with open(csvpath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    # Read the header row first (skip this step if there is now header)
    csv_header = next(csvreader)

    # initialize list variables
    months_list = []
    profits_list = []
    change_in_profit = []
    new_months_list = [] 
    
    # Read each row of data after the header
    for row in csvreader:

        # creat months list
        months_list.append(row[0])
        
        # create profit list
        profits_list.append(int(row[1]))
    
    # calculate the total number of months
    total_months = len(months_list)
   
    # calculate the total profits
    total_profits = sum(profits_list)
  
    #calculate change in profits month to month
    for i in range(len(profits_list) - 1):

        next_value = profits_list[i + 1]
        
        current_value = profits_list[i]
        
        change_in_profit.append(next_value - current_value)
        
        # create a new months list exluding the first month
        # this is done because the month to month change is calculated in the i + 1 month
        new_months_list.append(months_list[i + 1])

    # calculate the average change in profit
    average_change = round(sum(change_in_profit) / len(change_in_profit),2)
    
    # calculate the greatest increase in profit
    greatest_increase = max(change_in_profit)

    # calculate the greatest decrease in profit
    greatest_decrease = min(change_in_profit)
    
    # find date of greatest increase and decrease in profits

    # create dictionary of date:change in profit pairs
    profit_change_dict = dict(zip(new_months_list, change_in_profit))
    
    # search for months based on greatest increase and decrease criteria
    for key in profit_change_dict:

        # check each key value pair and check if value is equal to greatest increase
        if profit_change_dict[key] == greatest_increase:

            # return the month of greatest increase
            month_of_greatest_increase = key

        # check eash key value pair and check if value is equal to greatest decrease
        elif profit_change_dict[key] == greatest_decrease:

            # return the month of greatest decrease
            month_of_greatest_decrease = key
        

# print finanical analysis to terminal
print("Financial Analysis")
print("------------------------------")
print(f"Total Months: {total_months}")
print(f"Total Profit: ${total_profits}")
print(f"Average Change: ${average_change}")
print(f"Greatest Increase In Profits: {month_of_greatest_increase} (${greatest_increase})")
print(f"Greatest Decrease In Profits: {month_of_greatest_decrease} (${greatest_decrease})")
    
# write results to text file

# results file path
output_path = os.path.join("analysis", "PyBankResults.csv")

# Open the file using "write" mode.
with open(output_path, 'w', newline='') as csvfile:

    # Initialize csv.writer
    csvwriter = csv.writer(csvfile, delimiter=',')

    # Write analysis data to text file
    csvwriter.writerows([["Financial Analysis"],
                        ["------------------------"],
                        [f"Total Months: ${total_months}"],
                        [f"Total Profit: ${total_profits}"],
                        [f"Average Change: ${average_change}"],
                        [f"Greatest Increase In Profits: {month_of_greatest_increase} (${greatest_increase})"],
                        [f"Greatest Decrease In Profits: {month_of_greatest_decrease} (${greatest_decrease})"]])
