# add dependencies

import csv

import os

# Assign a variable to load a file fro a path
file_to_load = os.path.join("Resources", "election_results.csv")

# Assign a variable to save the file to a path
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Open the election results and read the file.
with open(file_to_load) as election_data:

    # Read the file object with the reader function.
    file_reader = csv.reader(election_data)

   # Read and print the header row.

    headers = next(file_reader)
    print(headers)




#write some data in the file
#with open(file_to_save, "w") as txt_file:
