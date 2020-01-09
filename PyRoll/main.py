import csv
import os

election_data_file = os.path.join(".",".","02-Homework","03-Python","Instructions","PyPoll","Resources","election_data.csv")

#create variables and lists

candidates = []
num_votes_cast = 0
vote_count = []

#read CSV and parse data into lists
with open(election_data_file, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)
    #Parse the votes
    for row in csvreader:
        #First question - total number of votes cast
        num_votes_cast += 1

        #grab the candidate's name
        candidate = row[2]

        #save the vote count to candidate
        if candidate in candidates:
            candidate_count = candidates.index(candidate)
            vote_count[candidate_count] =  vote_count[candidate_count] + 1
        else:
            candidates.append(candidate)
            vote_count.append(1)

#Variables for calculation
percentage = []
max_votes = vote_count [0]
max_index = 0

#calculating the # of votes for each candidate and finding the winner
for v_count in range(len(candidates)):
    v_percentage = vote_count[v_count]/num_votes_cast*100
    percentage.append(v_percentage)
    if vote_count[v_count] > max_votes:
        max_votes = vote_count[v_count]
        max_index = v_count
winner = candidates[max_index]

#round decimal
percentage = [round(i,2) for i in percentage]


homework_output= '/Users/macchina/Desktop/BootCamp/Boot/02-Homework/PyPoll_Output.txt'

with open (homework_output, 'w') as final_file:
    final_file.writelines('\n Election Results\n')
    final_file.writelines('_______________________________\n')
    final_file.writelines('Total Votes: ' + str(num_votes_cast) + '\n')
    final_file.writelines('_______________________________\n')
    for rep in range (len(candidates)):
        final_file.writelines(f'\n {candidates[rep]}: {percentage[rep]}% ({vote_count[rep]}) \n')
    final_file.writelines('\n'+'_______________________________\n')
    final_file.writelines(f'Winner: {winner} \n')
    final_file.writelines('_______________________________\n')


#print to terminal

with open(homework_output, 'r') as final_file_terminal:
    print(final_file_terminal.read())