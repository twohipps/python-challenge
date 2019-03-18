# Hipps
#----------------------------------------------
## PyBank
###############################################

# Import os module that has functions to interact with the file system
import os 
# Import module for reading CSV files
import csv 

# Import money data 
from statistics import mean
money = []
money2 = []

# Open file path
with open ('budget_data.csv') as csvfile:
    moneyreader = csv.reader(csvfile)
    next (moneyreader)
    for line in moneyreader:
        money.append(line)
        money2.append(int(line[1])) 

# Intialize variables
month= 0
for x in money:
    month += 1

total = 0 
for item in money2:
    total+= item
    
index1 = -1
greatest_index = 1
greatest_profit = money2[0]
for item in money2:
    index1 += 1
    if greatest_profit < item: 
        greatest_index = index1
        greatest_profit = item

lowest_profit = money2[0]
lowest_index = 0
index_2 = -1
for item in money2:
    index_2 += 1 
    if lowest_profit > item:
        lowest_profit = item
        lowest_index = index_2


changes = []
start = True
old_profit = 0
new_item = 0
for item in money2:
    if start == True:
        old_profit = item
    else:
        new_item = old_profit - item
        old_profit = item
        changes.append(new_item)
    start = False
average = mean(changes)
round_average = round(average,2)

## Display Results ##
# The total number of months included in the dataset
print('Financial Analysis')
print('----------------------------')
print('Total Months: %i' % month)
print('Average  Change: $%.2f' %round_average)
print('Greatest Increase in Profits: %s ($%s)' % (money[greatest_index][0], money[greatest_index][1]))
print('Greatest Decrease in Profits: %s ($%s)' % (money[lowest_index][0], money[lowest_index][1]))

f = open("test.txt","w+")
f.write('Financial Analysis\n')
f.write('----------------------------\n')
f.write('Total Months: %i\n' % month)
f.write('Average  Change: $%.2f\n' %round_average)
f.write('Greatest Increase in Profits: %s ($%s)\n' % (money[greatest_index][0], money[greatest_index][1]))
f.write('Greatest Decrease in Profits: %s ($%s)' % (money[lowest_index][0], money[lowest_index][1]))
f.close()

# print (month)
# print (total)
# print (greatest_index)
# print (greatest_profit)
# print (money[greatest_index][0])
# print (money[greatest_index][1])
# print (lowest_index)
# print (lowest_profit)
# print (money[lowest_index][01])
# print (money[lowest_index][1])


