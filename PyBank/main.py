#import modules
import os
import csv
from contextlib import redirect_stdout

#set up the path to locate the raw data
pybank_path = os.path.join('Resources','budget_data.csv')

#open target data file with read mode
with open(pybank_path,'r') as bankcsv:

    #set up a variable of the file and rows, columns split by ','
    csvreader = csv.reader(bankcsv, delimiter = ',')

    #skip the heading row for easy selecting and calculating data
    next(csvreader)

    #create lists to contain data of each date (every single row), all profit & loss value and the change value,
    #which is calculated as the value change between the current date and the previous date
    value_list = []
    row_list = []
    change_list = []

    #create iterator along the rows and adding elements into corresponding lists
    for row in csvreader:

        value_list.append(int(row[1]))
        row_list.append(row[0])

    #as mentioned above, there will be a calculation invovled of the value of current date, minus the value of 
    # previous date. As we have got a list of all values from above, so it could be convenient to think the list 
    # as a column in an excel file, just like the last VBA assignment. Hence, apply an iterator to perform the change 
    #of rows within the column to select the values and, do the math. The math, is to use the current row value, minus 
    #the previous row value, if start from row 1, which is the list[0], will return the error of not finding data. 
    #The trick here is to start one position after, as row 2, which is the list[1]. The value of Range[i] = value_list[i-1]
    # , and range(len(value_list)) will contain the last element within the value_list. Hence range(1, len(value_list))
    # is equal to [1,the length of the list == 86), where the value_list[85] = the last value in the list.
    for i in range(1,len(value_list)):

        change_list.append(value_list[i] - value_list[i-1])     #adding elements into the list
        change_avg = float(sum(change_list)/len(change_list))
        change_max = max(change_list)
        change_min = min(change_list)
        change_max_date = str(row_list[change_list.index(change_max)+1])    
        change_min_date = str(row_list[change_list.index(change_min)+1])
    
        #the reason of a '+1' in the above two lines is simple. The change_list position number is always 1 shorter than
        #the row_list, as it is the subtraction of the two values in the value_list. Say a list like [1,2,4], what is the 
        #subtraction of the values next to each other? The new list is [1,2]. And as the max and min value, occured only
        # at the current date, which, is the last number of this example, if you put the list in the right way, i.e.:
        # list: [1,2,4]
        # sub :   [1,2]
        #where in the programming language, it only shows:
        # list: [1,2,4]
        # sub : [1,2]
        #let's say, the answer of 2-1, is the first element in the sub list, but the last number of this equation is actually
        # the second number in the data list of [1,2,3]

    
    #print out all outcomes in the same layout as the given example from boot camp repo.
    print("Financial Analysis")
    print("------------------------------")   
    print(f"Total Months: {len(row_list)}")
    print(f"Total: ${sum(value_list)}")
    print("Average  Change: $%0.2f" %change_avg)
    print(f"Greatest Increase in Profits: {change_max_date} (${change_max})")
    print(f"Greatest Decrease in Profits: {change_min_date} (${change_min})")
    
    #close the file to release the control
    bankcsv.close()

#generate output to a text file under the targeted folder
output_path = os.path.join('Analysis','Pybank_Result.txt')

#open target data file with write mode
with open(output_path,'w') as f:
    with redirect_stdout(f):
        print("Financial Analysis")
        print("------------------------------")   
        print(f"Total Months: {len(row_list)}")
        print(f"Total: ${sum(value_list)}")
        print("Average  Change: $%0.2f" %change_avg)
        print(f"Greatest Increase in Profits: {change_max_date} (${change_max})")
        print(f"Greatest Decrease in Profits: {change_min_date} (${change_min})")

#close the file to release the control
f.close()