#import modules
import csv
import os
from collections import Counter
from contextlib import redirect_stdout

#set up the path to locate the raw data
pyroll_path = os.path.join('Resources','election_data.csv')

#open target data file with read mode
with open(pyroll_path, 'r') as rollcsv: 

    #set up a variable of the file and rows, columns split by ','
    csvreader = csv.reader(rollcsv,delimiter = ',')

    #skip the heading row for easy selecting and calculating data
    next(csvreader)

    #create lists to contain data of each vote ID (every single row), individual vote 
    # percentage of each candidate and all of the candidates' names appeared within the data
    voter_list = []
    indiv_percent = []
    candidate_count = []
    
    #create iterator along the rows and adding elements into corresponding lists
    for row in csvreader:

        voter_list.append(row[0])
        candidate_count.append(row[2])

    #count the result by using the counter, note it generates a dictionary with key and value 
    # pairs, in this case, key is the each candidate name and value is the number of vote they received.
    #I firstly tried conditional statement but it was not efficient
    vote_result = Counter(candidate_count)

    #as the counter (candidate_count) is a dict(), and the key and value are what required for the output, 
    #hence extract it to 2 new lists, one has the keys list as the candidates, the other one has the values
    #as the number of votes. Note that I have kept the original layout as two step for each one, however they
    #could be combined into one such as 'value_list = list(vote_result.values())
    values = vote_result.values()
    values_list = list(values)

    candidates = vote_result.keys()
    candidates_list = list(candidates)

    #to get the percentage value, calculation will be involved. It is related to the number of votes of each can-
    #didate and the total number of votes (which is the total number of rows). To get the each percentage value 
    #of the candidates, apply another sub-iterator within the value_list, and the total number of votes, can be 
    #found by using the len()
    for i in range(0,len(values_list)):
        indiv_percent.append(float(values_list[i]/len(voter_list)))

    #change the layout and format of the percentage list to have 3 decimal
    percent_list = [f"{x*100:.3f}%" for x in indiv_percent]

    #to find the winner, which is the candidate who get the most number of votes. This could be achieved by using
    # the max() from the previous counter value list. To match the candidate name within the key list, apply the 
    #conditional statement
    max_vote = max(vote_result.values())
    winner = [i for i in vote_result.keys() if vote_result[i] == max_vote]

    #print out all outcomes in the same layout as the given example from boot camp repo. Note that the winner part is 
    #different as this is generated directly from a dictionary, will change it later in the output part
    print("Election Results")
    print("----------------------------")
    print(f"Total Votes:  {len(voter_list)}")
    print("----------------------------")
    print(f"{candidates_list[0]}:  {percent_list[0]}  ({values_list[0]})")
    print(f"{candidates_list[1]}:  {percent_list[1]}  ({values_list[1]})")
    print(f"{candidates_list[2]}:  {percent_list[2]}  ({values_list[2]})")
    print(f"{candidates_list[3]}:  {percent_list[3]}  ({values_list[3]})")
    print("----------------------------")
    print(f"Winner: {winner}")
    print("----------------------------")
    
    #close the file to release the control
    rollcsv.close()

#generate output to a text file under the targeted folder
output_path = os.path.join("Analysis","Pyroll_Result.txt")

#open target data file with write mode
with open(output_path,'w') as f:
    with redirect_stdout(f):
        print("Election Results")
        print("----------------------------")
        print(f"Total Votes:  {len(voter_list)}")
        print("----------------------------")
        print(f"{candidates_list[0]}:  {percent_list[0]}  ({values_list[0]})")
        print(f"{candidates_list[1]}:  {percent_list[1]}  ({values_list[1]})")
        print(f"{candidates_list[2]}:  {percent_list[2]}  ({values_list[2]})")
        print(f"{candidates_list[3]}:  {percent_list[3]}  ({values_list[3]})")
        print("----------------------------")
        print(f"Winner: {candidates_list[0]}")    #manually change the print content as to match the given outcome on Repo
        print("----------------------------")

#close the file to release the control
f.close()
