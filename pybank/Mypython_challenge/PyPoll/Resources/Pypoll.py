import os
import csv
election_data_csv = os.path.join("PyPoll","Resources", "election_data.csv")
election_data_txt = os.path.join("PyPoll","output", "election_data.csv")
#list of dstas/tracking datas
total_number = 0
candidates_options = []
candidates_votes = {}
winning_candidates = ""
winning_count = 0

with open(election_data_csv) as electionfile:
    csvreader = csv.reader(electionfile, delimiter=",")
    #header = next(csvreader)
    firstrow = next(csvreader)
    #initial_election = int(firstrow[1])

    for row in csvreader:
        #total number 
        total_number +=1
        #print("row:", row)
        #Collecting candidates names from each role

        candidate_name = row[2]
        #print(candidate_name)
        #if candidate is not/match any existing list
        if candidate_name  not in candidates_options:
            #Add to the list
            candidates_options.append(candidate_name)
            #lookout for the candidate voter count
            candidates_votes[candidate_name] = 0
            #Adding votes to the canadidates count
            candidates_votes[candidate_name] = candidates_votes[candidate_name] + 1
        else:
            candidates_votes[candidate_name] = candidates_votes[candidate_name] + 1
         
Result = (
f"Election Results\n"
f"------------------\n"
f"Total Votes: {total_number}\n"
f"------------------\n"
)
print(Result)  
with open(election_data_txt, "w") as outfile:
    outfile.write(Result)        
             #To determine the vote count& %
for candidate in candidates_votes:
         votes = candidates_votes.get(candidate)
        # print("candidate:", candidate)
         #print("votes:", votes)
         vote_percentage = float(votes)/ float(total_number) * 100
         #print("Vote_percentage:", vote_percentage)
         #print(candidate vote_percentage {(votes)})
    # to determine the winning vote and winner
         if (votes > winning_count):
              winning_candidates = candidate
              winning_count = votes

         #print(candidate, vote_percentage)
         Result_2 = (

         f"{candidate}: {vote_percentage: .3f}% ({votes}\n"
)
         print(Result_2)
         with open(election_data_txt, "a") as outfile:
           outfile.write(Result_2)  
Result_3=(
f"------------------\n"        
f"Winner:{winning_candidates}\n"
)
print(Result_3)
with open(election_data_txt, "a") as outfile:
    outfile.write(Result_3)   

#print("candidates_votes:",candidates_votes)
#print("candidates_options:",candidates_options)


         



