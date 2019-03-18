import os
import csv


Election_Analysis = []
voters1 = []
candidates1 = []
candidate_list1 = []


Khan = 0
Correy = 0
Li = 0
OTooley = 0

with open ('election_data_1.csv') as csvfile:
    csv_reader1 = csv.reader(csvfile, delimiter=",")
    next(csv_reader1, None)
    for line in csv_reader1:
        voters1.append(line[0])
        candidates1.append(line[2])
        total_votes1 = len(voters1)
    
    for line in csv_reader1:
        voters1.append(line[0])
        candidates1.append(line[2])
        total_votes1 = len(voters1)
    for i in candidates1:
        if i not in candidate_list1:
            candidate_list1.append(i)
        elif i == 'Khan':
            Khan = Khan + 1
        elif i == 'Correy':
            Correy = Correy + 1
        elif i == 'Li':
            Li = Li + 1
        elif i == "O'Tooley":
            OTooley = OTooley + 1
        Khan_perc = Khan/total_votes1
        Correy_perc = Correy/total_votes1
        Li_perc =Li/total_votes1    
        OTooley_perc = OTooley/total_votes1

total_votes = total_votes1

Khan_perc = Khan/total_votes
Correy_perc = Correy/total_votes
Li_perc = Li/total_votes    
OTooley_perc = OTooley/total_votes

Election_Analysis = [Khan, Correy, Li, OTooley]
Election_Perc = [Khan_perc, Correy_perc, Li_perc, OTooley_perc]
Winner = max(Election_Analysis)

'''
dictionary = dict(zip(candidate_list, Election_Analysis))
for keys, values in dictionary.items():
    print(keys, values)
    
'''


Election_Results = os.path.join("Election_Results.csv")
with open(Election_Results, 'w', newline="") as datafile:
    csvWriter = csv.writer(datafile)
    csvWriter.writeline(["Election Results"])
    csvWriter.writeline(["----------------------------"])
    csvWriter.writeline(["Total Votes: " + str(total_votes)])
    csvWriter.writeline(["----------------------------"])
    csvWriter.writeline(["Khan: " + str(round(Khan_perc*100, 0)) + "%" + " (" + str(Khan) + ")"])
    csvWriter.writeline(["Correy: " + str(round(Correy_perc*100, 0)) + "%" + " (" +  str(Correy) + ")"])
    csvWriter.writeline(["Li: " + str(round(Li_perc*100, 0)) + "%" + " (" + str(Li) + ")"])
    csvWriter.writeline(["O'Tooley: " + str(round(OTooley_perc*100, 0)) + "%" + " (" + str(OTooley) + ")"])
    csvWriter.writeline(["----------------------------"])
    csvWriter.writeline(["Winner: " + str(candidate_list[Election_Analysis.index(max(Election_Analysis))])])
    csvWriter.writeline(["----------------------------"])

Election_Analysis = [Khan_perc, Correy_perc, Li_perc, OTooley_perc]
Winner = max(Election_Analysis)

print("Election Results")
print("----------------------------")
print("Total Votes: " + str(total_votes))
print("----------------------------")
print("Khan: " + str(round(Khan_perc*100, 0)) + "% " + "(" + str(Khan) + ")")
print("Correy: " + str(round(Correy_perc*100, 0)) + "% " + "(" + str(Correy) + ")")
print("Li: " + str(round(Li_perc*100, 0)) + "% " + "(" + str(Li) + ")")
print("O'Tooley: " + str(round(OTooley_perc*100, 0)) + "% " + " (" + str(OTooley) + ")")
print("----------------------------")
print("Winner: " + str(candidate_list[Election_Analysis.index(max(Election_Analysis))]))
print("----------------------------")

