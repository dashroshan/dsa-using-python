"""
Find index of all the occurances of a number from sorted list

numbers = [1,4,6,9,11,15,15,15,17,21,34,34,56]
number_to_find = 15  
This should return 5,6,7 as indices containing number 15 in the array
"""


def binary_search(numbers_list, number_to_find):
    left_index = 0
    right_index = len(numbers_list) - 1
    mid_index = 0

    while left_index <= right_index:
        mid_index = (left_index + right_index) // 2
        mid_number = numbers_list[mid_index]

        if mid_number == number_to_find:
            temp = mid_index
            indexList = []
            while numbers_list[temp] == number_to_find:
                indexList.append(temp)
                temp -= 1
            temp = mid_index + 1
            while numbers_list[temp] == number_to_find:
                indexList.append(temp)
                temp += 1
            return indexList

        if mid_number < number_to_find:
            left_index = mid_index + 1
        else:
            right_index = mid_index - 1

    return -1


numbers = [1, 4, 6, 9, 11, 15, 15, 15, 17, 21, 34, 34, 56]
number_to_find = 15
print(binary_search(numbers, number_to_find))
