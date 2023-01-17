import os
import csv

budget = os.path. join("Resources", "budget_data.csv")

date = []
profit = []
change = []

with open (budget, encoding='utf-8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    header = next(csvreader)

    for row in csvreader:
        date.append(row[0])

        profit.append(int(row[1]))
        
os.mkdir("Analysis")
result = os.path.join ("Analysis", "result_PyBank.txt")

for x, row in enumerate (profit):
    if x>0:
        change.append(profit[x]-profit[x-1])


with open (result, "w") as f:
    
    f.write("Financial Analysis \n")    
    f.write("------------------\n")
    f.write("Total Months: " + str(len(date)) + "\n")
    f.write("Total: " + "$" + str(sum(profit)) + "\n")
    f.write("Average Change: " + "$" + str(round(sum(change)/len(change), 2)) + '\n')

print("Financial Analysis")
print("------------------")
print(f"Total Months: {len(date)}")
print(f"Total : ${sum(profit)}")

date.pop(0)
print(f"Average Change: ${round(sum(change)/len(change), 2)}")

for i, row in enumerate(change):
    
    if change [i]>=max(change):
        with open(result, 'a') as f:
            f.write("Greatest Increase in Profits:" + str(date[i]) + "($"+ str(max(change))+ " \n")
        print(f"Greatest Increase in Profits: {date[i]} (${max(change)})")   
        
   
    if change [i]<=min(change):
        with open(result, 'a') as f:
            f.write("Greatest Decrease in Profits:" + str(date[i]) + "($" + str(min(change))+ " \n")  
        print(f"Greatest Decrease in Profits: {date[i]} (${min(change)})")

