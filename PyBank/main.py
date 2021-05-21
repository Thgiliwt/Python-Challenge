import os
import csv

pybank_path = os.path.join('Resources','budget_data.csv')

with open(pybank_path,'r') as bankcsv:

    csvreader = csv.reader(bankcsv, delimiter = ',')

    print("Financial Analysis")
    print("------------------------------")   
    
    row_count = len(list(csvreader)) - 1

    bankcsv.seek(0)

    next(csvreader)
    value_sum = 0

    for row in csvreader:

        value_sum = value_sum + int(row[1])

    

    

    
    print(f"Total Months: {row_count}")
    print(f"Total: ${value_sum}")