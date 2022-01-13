"""
Create a list of all odd numbers between 1 and a max number. Max number is
something you need to take from a user using input() function
"""

maxNum = int(input("Enter the max number : "))
listOfOdd = []
for number in range(1, maxNum + 1, 2):
    listOfOdd.append(number)
print(listOfOdd)
