# add dependencies

import csv

import os

# Assign a variable to load a file fro a path
file_to_load = os.path.join("Resources", "election_results.csv")

# Assign a variable to save the file to a path
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Initialize a total vote counter
total_votes = 0

# Initializing list of candidates
candidate_options = []

# Initializing vote-tallying Dictionary
candidate_votes = {}

# Winning candidate and winning count tracker
winning_candidate =""
winning_count = 0
winning_percentage = 0

# Open the election results and read the file.
with open(file_to_load) as election_data:

    # Read the file object with the reader function.
    file_reader = csv.reader(election_data)

   # Read and print the header row.

    headers = next(file_reader)
    print(headers)

    # print(headers)

    # Loop through each row in the CSV file
    for row in file_reader:
        # Add to the total vote count
        total_votes += 1

        # print candidate name from each row
        candidate_name = row[2]

        # add candidate name to candidate list IF NOT already listed
        if candidate_name not in candidate_options:
            candidate_options.append(candidate_name)

            # begin tracking vota count (setting count to 0)
            candidate_votes[candidate_name]=0

        # add up candidate votes
        candidate_votes[candidate_name] += 1


# Print the total votes
print(total_votes)
# Print candidate options
print(candidate_options)
# Print candidate_votes dictionare
print(candidate_votes)

# determining the percentage of the vote for each candidate
for candidate_name in candidate_votes:

    votes = candidate_votes[candidate_name]

    vote_percentage = votes / total_votes * 100

    # print(f'{candidate_name} received {vote_percentage:.1f}% of the vote.')

    #pring candidate name and vote stats
    print(f'{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n')

    if (votes > winning_count) and (vote_percentage > winning_percentage):

        winning_count = votes

        winning_percentage = vote_percentage

        winning_candidate = candidate_name


winning_candidate_summary = (
    f'-----------------------------\n'
    f'Winner: {winning_candidate}\n'
    f'Winning Vote Count: {winning_count:,}\n'
    f'Winning Percentage: {winning_percentage:.1f}%\n'
    f'-----------------------------\n')

print(winning_candidate_summary)

#print(f'The winning candidate is {winning_candidate} with {winning_count} votes and {winning_percentage:.1f}% of the total votes.')
