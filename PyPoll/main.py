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
    candidate_name_list = []
    vote_count_list = []
    vote_percent_list = []

    # Read each row of data after the header
    for row in csvreader:
        
        candidate_list.append(row[2])

        candidate_name = row[2]

        if candidate_name not in candidate_name_list:
            candidate_name_list.append(candidate_name)
        
    for name in candidate_name_list:
        vote_count_list.append(candidate_list.count(name))

    total_votes = len(candidate_list)
    
    for votes in vote_count_list:
        vote_percent_list.append(round((votes / total_votes) * 100, 3))

    vote_count_dict = dict(zip(candidate_name_list, vote_count_list))

    # print(vote_count_dict)

    #print(f"{candidate_name_list[0]} {votes_count_dict[candidate_name_list[0]]}")

    max_votes = max(vote_count_list)

    for key in vote_count_dict:
        if vote_count_dict[key] == max_votes:
            winner = key

    print("Election Results")
    print("--------------------------")
    print(f"Total Votes: {total_votes}")
    print("--------------------------")
    print(f"{candidate_name_list[0]}: {vote_percent_list[0]}% ({vote_count_list[0]})")
    print(f"{candidate_name_list[1]}: {vote_percent_list[1]}% ({vote_count_list[1]})")
    print(f"{candidate_name_list[2]}: {vote_percent_list[2]}% ({vote_count_list[2]})")
    print(f"{candidate_name_list[3]}: {vote_percent_list[3]}% ({vote_count_list[3]})")
    print("--------------------------")
    print(f"Winner: {winner}")
    print("--------------------------")

# results file path
output_path = os.path.join("analysis", "results.csv")

# Open the file using "write" mode.
with open(output_path, 'w', newline='') as csvfile:

    # Initialize csv.writer
    csvwriter = csv.writer(csvfile, delimiter=',')

    # Write analysis data to text file
    csvwriter.writerows([["Election Results"],
                        ["--------------------------"],
                        [f"Total Votes: {total_votes}"],
                        ["--------------------------"],
                        [f"{candidate_name_list[0]}: {vote_percent_list[0]}% ({vote_count_list[0]})"],
                        [f"{candidate_name_list[1]}: {vote_percent_list[1]}% ({vote_count_list[1]})"],
                        [f"{candidate_name_list[2]}: {vote_percent_list[2]}% ({vote_count_list[2]})"],
                        [f"{candidate_name_list[3]}: {vote_percent_list[3]}% ({vote_count_list[3]})"],
                        ["--------------------------"],
                        [f"Winner: {winner}"],
                        ["--------------------------"]])