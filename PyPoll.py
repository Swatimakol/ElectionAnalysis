from datetime import date, time, datetime
import csv
import os
dir(os)
dir(csv)


# This will get the time and date 
# now = datetime.now()
# print("The time is " + str(now))

# first we will open the file 
file_to_load = os.path.join("Project", "election_result.csv")

# to make sure it saves to a text file
file_to_save = os.path.join("Project", "election_analysis.txt")

# Intial total votes before opening the csv 

total_votes = 0

# Canditae options
candidate_options = []

# Now we declare a dictionary
candidate_votes = {}

#for finding the winning candidate
winning_candidate = ""
winning_votes = 0
winning_percentage = 0

#start readingt he csv file
with open(file_to_load) as election_data:
   # print(election_data)
   
# Now we read and analyze our data

    file_reader = csv.reader(election_data)
    
    headers = next(file_reader)
    
    print(headers)
    
    for row in file_reader:
        total_votes +=1
    
        candidate_names = row[2]
    
        if candidate_names not in candidate_options:
        
            candidate_options.append(candidate_names)
            
            candidate_votes[candidate_names] = 0
    
        candidate_votes[candidate_names] += 1
        
with open(file_to_save, "w") as txt_file:
    election_results = (
        f"\nElection Results\n"
        f"-----------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-----------------------\n"
        
    )
    
    print(election_results, end="")
    txt_file.write(election_results)
        
    for candidate_names in candidate_votes:
        votes = candidate_votes[candidate_names]
    # 3. Calculate the percentage of votes.
        vote_percentage = float(votes) / float(total_votes) * 100
    # 4. Print the candidate name and percentage of votes.
       # print(f"{candidate_names}:{vote_percentage:.1f}% ({votes:,})\n")
        candidate_results =(f"{candidate_names}: {vote_percentage:.1f}% ({votes:,})\n")
        print(candidate_results)
        txt_file.write(candidate_results) 
        
        if(votes > winning_votes) and (vote_percentage > winning_percentage):
            winning_votes = votes
            winning_percentage = vote_percentage
            winning_candidate = candidate_names
        #print(f"{candidate_names}: {vote_percentage:.1f}% ({votes:,})\n")
        
    winning_candidate_summary = (
    f"-------------------------\n"
    f"Winner: {winning_candidate}\n"
    f"Winning Vote Count: {winning_votes:,}\n"
    f"Winning Percentage: {winning_percentage:.1f}%\n"
    f"-------------------------\n")
    print(winning_candidate_summary)
    txt_file.write(winning_candidate_summary)
     
    #print(candidate_options)
    #print(candidate_votes)
    
        

# Using the open() function with the "w" mode 
# we will write data to the file.
#-----comenting it out for no
#with open(file_to_save, "w") as txt_file:
    #txt_file.write("Hello World")



