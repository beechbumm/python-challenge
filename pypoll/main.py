import csv
import os

# Path to the input file
file_path = 'pypoll/Resources/election_data.csv'

# Initialize variables
total_votes = 0
candidate_votes = {}

# Read the CSV file and count the votes for each candidate
with open(file_path, 'r') as file:
    csvreader = csv.reader(file)
    next(csvreader)  # Skip header row
    for row in csvreader:
        total_votes += 1
        candidate = row[2]
        candidate_votes[candidate] = candidate_votes.get(candidate, 0) + 1

# Calculate the winner
winner = max(candidate_votes, key=candidate_votes.get)




# Print analysis to the terminal
print("Election Results")
print("-------------------------")
print(f"Total Votes: {total_votes}")
print("-------------------------")
for candidate, votes in candidate_votes.items():
    percentage = (votes / total_votes) * 100
    print(f"{candidate}: {percentage:.3f}% ({votes})")
print("-------------------------")
print(f"Winner: {winner}")
print("-------------------------")

# Export results to a text file
output_file = 'pypoll/analysis/election_results.txt'

with open(output_file, 'w') as file:
    file.write("Election Results\n")
    file.write("-------------------------\n")
    file.write(f"Total Votes: {total_votes}\n")
    file.write("-------------------------\n")
    for candidate, votes in candidate_votes.items():
        percentage = (votes / total_votes) * 100
        file.write(f"{candidate}: {percentage:.3f}% ({votes})\n")
    file.write("-------------------------\n")
    file.write(f"Winner: {winner}\n")
    file.write("-------------------------\n")

print(f"Analysis results have been exported to {output_file}")