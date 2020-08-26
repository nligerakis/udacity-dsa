"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

numberCounts = {}
for send, receive, time in texts:
    numberCounts[send] = numberCounts.get(send, 0) + 1
    numberCounts[receive] = numberCounts.get(receive, 0) + 1

for send, receive, time, duration in calls:
    numberCounts[send] = numberCounts.get(send, 0) + 1
    numberCounts[receive] = numberCounts.get(receive, 0) + 1

print(f'There are {len(numberCounts)} different telephone numbers in the records')

"""
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."
"""
