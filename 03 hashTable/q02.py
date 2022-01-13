"""
nyc_weather.csv contains new york city weather for first few days in the month
of January. Write a program that can answer following,

What was the temperature on Jan 9?
What was the temperature on Jan 4?

Figure out data structure that is best for this problem
"""

import csv

data = {}
with open("03 hashTable/dataSet/nyc_weather.csv", mode="r") as csvFile:
    csvReader = csv.reader(csvFile, delimiter=",")
    next(csvReader)
    for row in csvReader:
        data[int(row[0].split()[1])] = int(row[1])

print(f"Temperature on Jan 9 is {data[9]}")
print(f"Temperature on Jan 4 is {data[4]}")
