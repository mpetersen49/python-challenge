# python script for PyPoll problem

# import modules
import os
import csv

# set file path for data file
csvpath = os.path.join("Resources","election_data.csv")

with open(csvpath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    # Read the header row first (skip this step if there is now header)
    csv_header = next(csvreader)
    
    candidate_list = []


    # Read each row of data after the header
    for row in csvreader:
        
        candidate_list.append(row[2])

    total_votes = len(candidate_list)

    print(f"Total Votes: {total_votes}")