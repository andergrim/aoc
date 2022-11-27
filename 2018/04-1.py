import re

with open("04-1.txt", "r") as f:
    timestamps = f.readlines() 

timestamps.sort()
for log in timestamps:
    day, time, action = re.match("\[(\d\d\d\d\-\d\d\-\d\d) (\d\d\:\d\d)\] (.*)", log).groups()
    print(day, time, action)
