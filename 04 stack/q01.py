"""
Write a function in python that can reverse a string using stack data structure.
Use Stack class from the tutorial.

reverse_string("We will conquere COVID-19")
should return "91-DIVOC ereuqnoc lliw eW"
"""

from collections import deque


class Stack:
    def __init__(self):
        self.container = deque()

    def push(self, value):
        self.container.append(value)

    def pop(self):
        return self.container.pop()

    def peek(self):
        return self.container[-1]

    def size(self):
        return len(self.container)


def reverse_string(string):
    s = Stack()
    for char in string:
        s.push(char)
    reversed = ""
    while s.size():
        reversed += s.pop()
    return reversed


print(reverse_string("We will conquere COVID-19"))
