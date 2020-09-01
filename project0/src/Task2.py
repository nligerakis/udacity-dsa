"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

longestTime = 0
number = ""
times = {}
for call in calls:
    caller = call[0]
    receiver = call[1]
    length = int(call[3])
    times[caller] = times.get(caller, 0) + length
    times[receiver] = times.get(receiver, 0) + length

sortCalls = sorted(times.items(), key=lambda x: x[1], reverse=True)



print(f'{sortCalls[0][0]} spent the longest time, {sortCalls[0][1]} seconds, on the phone during September 2016.')

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""

