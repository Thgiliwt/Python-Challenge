import os
import csv

pybank_path = os.path.join('Resources','budget_data.csv')

with open(pybank_path,'r') as bankcsv:

    csvreader = csv.reader(bankcsv, delimiter = ',')

    next(csvreader)

    value_list = []
    row_list = []
    change_list = []

    for row in csvreader:

        value_list.append(int(row[1]))
        row_list.append(row[0])


    for i in range(1,len(value_list)):

        change_list.append(value_list[i] - value_list[i-1])
        change_avg = float(sum(change_list)/len(change_list))
        change_max = max(change_list)
        change_min = min(change_list)
        change_max_date = str(row_list[change_list.index(change_max)+1])
        change_min_date = str(row_list[change_list.index(change_min)+1])
    
    #Below is my initial method where due to the change of pointer position, I have to keep adding '.seek(0)' to replace it back to starting position.
    
    # row_count = len(list(csvreader)) - 1

    # bankcsv.seek(0)

    
    # next(csvreader)
    
    # value_sum = 0
    
    # for row in csvreader:

    #     value_sum = value_sum + int(row[1])

    # bankcsv.seek(0)  

    

    

    print("Financial Analysis")
    print("------------------------------")   
    print(f"Total Months: {len(row_list)}")
    print(f"Total: ${sum(value_list)}")
    print("Average  Change: $%0.2f" %change_avg)
    print(f"Greatest Increase in Profits: {change_max_date} (${change_max})")
    print(f"Greatest Decrease in Profits: {change_min_date} (${change_min})")
    bankcsv.close()