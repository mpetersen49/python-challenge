# python script for PyPoll problem

# import modules
import os
import csv

# set file path for data file
csvpath = os.path.join("Resources","election_data.csv")

# open csv
with open(csvpath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    # Read the header row first
    csv_header = next(csvreader)
    
    # initiate lists to hold data from csv file
    vote_list = []
    candidate_name_list = []
    vote_count_list = []
    vote_percent_list = []
    text_list = []

    # Read each row of data after the header
    for row in csvreader:
        
        # create list of votes
        vote_list.append(row[2])

        # iterate through candidate names
        candidate_name = row[2]

        # check if name is unique and put into candidate_name_list
        if candidate_name not in candidate_name_list:

            # list of unique candidates
            candidate_name_list.append(candidate_name)

    # iterate through unique candidate names and count votes for each    
    for name in candidate_name_list:
        vote_count_list.append(vote_list.count(name))

    # calculate total votes
    total_votes = len(vote_list)
    
    # calculate percentage of votes earned by each candidate
    for votes in vote_count_list:
        vote_percent_list.append(round((votes / total_votes) * 100, 3))

    # create dictionary of candidate:vote count pairs - used to find winner
    vote_count_dict = dict(zip(candidate_name_list, vote_count_list))

    # calculate the max vote count
    max_votes = max(vote_count_list)

    # find the winnding candidate based on max vote count
    for key in vote_count_dict:
        if vote_count_dict[key] == max_votes:
            winner = key
    
    # count the number of unique candidates - used for printing results
    num_of_candidates = len(candidate_name_list)

    # print election results to terminal
    print("Election Results")
    print("--------------------------")
    print(f"Total Votes: {total_votes}")
    print("--------------------------")

    # iterate through unique candidates to write unique candidate results
    for i in range(num_of_candidates):
        
        # print to terminal
        print(f"{candidate_name_list[i]}: {'{:.3f}'.format(vote_percent_list[i])}% ({vote_count_list[i]})")
        
        # creates text list to be used to write to text file
        text_list.append(f"{candidate_name_list[i]}: {'{:.3f}'.format(vote_percent_list[i])}% ({vote_count_list[i]})")

    print("--------------------------")
    print(f"Winner: {winner}")
    print("--------------------------")

# write election results to text file

# results file path
output_path = os.path.join("analysis", "PyPollResults.csv")

# Open the file using "write" mode.
with open(output_path, 'w', newline='') as csvfile:

    # Initialize csv.writer
    csvwriter = csv.writer(csvfile, delimiter=',')

    # zip the text list for writing to text file
    zipped_text = zip(text_list)

    # Write analysis data to text file
    csvwriter.writerows([["Election Results"],
                        ["--------------------------"],
                        [f"Total Votes: {total_votes}"],
                        ["--------------------------"]])

    # iterate zipped text list to write unique candidate results
    csvwriter.writerows(zipped_text)
                        
    csvwriter.writerows([["--------------------------"],
                        [f"Winner: {winner}"],
                        ["--------------------------"]])