# Import Dependencies
import csv
import os

# Variable declaration
container = []

# Create reference path to CSV in_file and TXT out_file
csv_in_path = os.path.join('PyBank','Resources','budget_data.csv')
txt_out_path = os.path.join('PyBank','Analysis','analyzed_budget_data.txt')

# Open the CSV as in_file
with open(csv_in_path, 'r') as in_file:
    reader = csv.reader(in_file)
    next(reader)
    current_pnl = 0
    for row in reader:
        container.append(row)

# List comprehensions to solve the challenge
months = [i[0] for i in container] 
pnl = [int(i[1]) for i in container]
# Create a zipped object to calculate the changes in profit / loss
delta = [j - i for i, j in zip(pnl, pnl[1:])]
# Create a zipped object and sort in ascending order via sorted() function
cleaned_list = zip(delta, months[1:])
sorted_cleaned_list = sorted(cleaned_list)

# Print results to console
print('Financial Analysis\n-------------------')
print(f'Total Months: {len(set(months))}')
print(f'Total: ${sum(pnl)}')
print(f'Average Change: ${round(sum(delta)/len(delta),2)}')
print(f'Greatest Increase in Profits: {sorted_cleaned_list[-1][1]} (${sorted_cleaned_list[-1][0]})')
print(f'Greatest Decrease in Profits: {sorted_cleaned_list[0][1]} (${sorted_cleaned_list[0][0]})')

# Print results to txt file
print('Financial Analysis\n-------------------', file=open(txt_out_path, 'w'))
print(f'Total Months: {len(set(months))}', file=open(txt_out_path, 'a'))
print(f'Total: ${sum(pnl)}', file=open(txt_out_path, 'a'))
print(f'Average Change: ${round(sum(delta)/len(delta),2)}', file=open(txt_out_path, 'a'))
print(f'Greatest Increase in Profits: {sorted_cleaned_list[-1][1]} (${sorted_cleaned_list[-1][0]})', file=open(txt_out_path, 'a'))
print(f'Greatest Decrease in Profits: {sorted_cleaned_list[0][1]} (${sorted_cleaned_list[0][0]})', file=open(txt_out_path, 'a'))