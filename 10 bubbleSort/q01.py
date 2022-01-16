"""
Qs : https://github.com/codebasics/data-structures-algorithms-python/blob/master/algorithms/2_BubbleSort/bubble_sort_exercise.md
"""


def bubbleSort(list, key):
    for i in range(len(list)):
        for j in range(len(list) - 1):
            if list[j][key] > list[j + 1][key]:
                list[j], list[j + 1] = list[j + 1], list[j]
    return list


elements = [
    {"name": "mona", "transaction_amount": 1000, "device": "iphone-10"},
    {"name": "dhaval", "transaction_amount": 400, "device": "google pixel"},
    {"name": "kathy", "transaction_amount": 200, "device": "vivo"},
    {"name": "aamir", "transaction_amount": 800, "device": "iphone-8"},
]
print(bubbleSort(elements, key="transaction_amount"))
