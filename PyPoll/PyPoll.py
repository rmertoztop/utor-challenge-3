import os
import csv

election = os.path. join("Resources","election_data.csv")


voter = []
county = []
candidate = []
count2 = 0
winnerName = ""


with open (election, encoding='utf-8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    header = next(csvreader)

    for row in csvreader:
        voter.append(row[0])
        county.append(row[1])
        candidate.append(row[2])

totalVote = len(candidate)

selectUniqueNameList = list(dict.fromkeys(candidate))

os.mkdir("Analysis")
result = os.path.join ("Analysis","result_PyPoll.txt")
with open (result, "w") as f:

    f.write("Election Results \n")
    f.write("------------------------------------\n")
    f.write("Total Votes: " + str(totalVote) + "\n")
    

print("Election Results")
print("------------------------------------")
print("Total Votes: ", totalVote)
print("------------------------------------")


for uniqueName in selectUniqueNameList:

    count = 0
    for name in candidate:
        if (uniqueName == name):
            count = count + 1
    if (count > count2):
        count2 = count
        winnerName = uniqueName

    votePercent = count / totalVote * 100

# f.write(format(uniqueName, (round(votePercent,3)), (count)))
    print("{}: {}% ({}) ".format(uniqueName, round(votePercent,3), count))


with open (result, "a") as f:

    # f.write("():"+ "()%" +"(())"+str(format(uniqueName+ str(round(votePercent,3))+ str(count))))
    f.write("------------------------------------\n")
    f.write("Winner: " + str(winnerName) + "\n")
    f.write("------------------------------------\n")


print("------------------------------------")
print("Winner: ", winnerName)
print("------------------------------------")