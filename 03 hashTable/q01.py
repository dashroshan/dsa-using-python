"""
nyc_weather.csv contains new york city weather for first few days in the month
of January. Write a program that can answer following,

What was the average temperature in first week of Jan
What was the maximum temperature in first 10 days of Jan

Figure out data structure that is best for this problem
"""

import csv

data = {}
with open("03 hashTable/dataSet/nyc_weather.csv", mode="r") as csvFile:
    csvReader = csv.reader(csvFile, delimiter=",")
    next(csvReader)
    for row in csvReader:
        data[int(row[0].split()[1])] = int(row[1])

avg1stWeek = 0
for day in range(1, 8):
    avg1stWeek += data[day]
avg1stWeek /= 7

maxTemp = -100
for day in range(1, 11):
    maxTemp = data[day] if data[day] > maxTemp else maxTemp

print(f"Average temperature in first week of Jan is {round(avg1stWeek,2)}")
print(f"Maximum temperature in first 10 days of Jan is {maxTemp}")
