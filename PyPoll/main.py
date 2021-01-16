# Import Dependencies
import csv
import os
from collections import Counter

# Variable declaration
candidates = []

# Create reference path to CSV in_file and TXT out_file
csv_in_path = os.path.join('PyPoll','Resources','election_data.csv')
txt_out_path = os.path.join('PyPoll','Analysis','analyzed_election_data.txt')

# Open the CSV as in_file
with open(csv_in_path, 'r') as in_file:
    reader = csv.reader(in_file)
    next(reader)
    votes_count = 0
    for row in reader:
        candidates.append(row[2])

# Use Counter function to summarize the list
container = Counter(candidates)

# Print results to console
print('Election Results\n-------------------')
print(sum(container.values()))
print('-------------------')
# Print dict key, value pairs and calculate the percentage based on sum() of container values
for key, value in container.items():
    print(f'{key}: {round(value/sum(container.values())*100,3)}% ({value})')
print('-------------------')
print(f'Winner: {list(container.keys())[0]}')
print('-------------------')

# Print results to txt file
print('Election Results\n-------------------', file=open(txt_out_path, 'w'))
print(sum(container.values()), file=open(txt_out_path, 'a'))
print('-------------------', file=open(txt_out_path, 'a'))
for key, value in container.items():
    print(f'{key}: {round(value/sum(container.values())*100,3)}% ({value})', file=open(txt_out_path, 'a'))
print('-------------------', file=open(txt_out_path, 'a'))
print(f'Winner: {list(container.keys())[0]}', file=open(txt_out_path, 'a'))
print('-------------------', file=open(txt_out_path, 'a'))