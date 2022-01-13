"""
poem.txt Contains famous poem "Road not taken" by poet Robert Frost. You have to
read this file in python and print every word and its count as show below. Think
about the best data structure that you can use to solve this problem and figure
out why you selected that specific data structure.

'diverged': 2,
'in': 3,
'I': 8
"""

data = {}

with open("03 hashTable/dataSet/poem.txt", mode="r") as poemFile:
    lines = poemFile.readlines()
    for line in lines:
        words = line.split()
        for word in words:
            if (data.get(word, None)) == None:
                data[word] = 1
            else:
                data[word] += 1

for key, value in data.items():
    print(f"'{key}': {value},")
