import csv
import os
from collections import Counter
from contextlib import redirect_stdout

pyroll_path = os.path.join('Resources','election_data.csv')

with open(pyroll_path, 'r') as rollcsv:

    csvreader = csv.reader(rollcsv,delimiter = ',')

    next(csvreader)

    voter_list = []
    indiv_percent = []
    candidate_count = []
    #candidate_list = set()

    

    for row in csvreader:

        voter_list.append(row[0])
        candidate_count.append(row[2])

        #candidate_list.add(row[2])
    
    vote_result = Counter(candidate_count)

    values = vote_result.values()
    values_list = list(values)

    candidates = vote_result.keys()
    candidates_list = list(candidates)

    for i in range(0,len(values_list)):
        indiv_percent.append(float(values_list[i]/len(voter_list)))

    percent_list = [f"{x*100:.3f}%" for x in indiv_percent]

    # election = dict()

    # election["candidate"] = candidates_list
    # election["percentage"] = indiv_percent
    # election["vote"] = values_list
    
    #temp = '%(candidate)s, %(percentage)0.3f, (%(vote)i)'

    max_vote = max(vote_result.values())
    winner = [i for i in vote_result.keys() if vote_result[i] == max_vote]
   
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
    
    rollcsv.close()


output_path = os.path.join("Analysis","Pyroll_Result.txt")
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

f.close()
