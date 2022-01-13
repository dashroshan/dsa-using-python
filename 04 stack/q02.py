"""
Write a function in python that checks if paranthesis in the string are balanced
or not. Possible parantheses are "{}',"()" or "[]". Use Stack class from the
tutorial.

is_balanced("({a+b})")     --> True
is_balanced("))((a+b}{")   --> False
is_balanced("((a+b))")     --> True
is_balanced("))")          --> False
is_balanced("[a+b]*(x+2y)*{gg+kk}") --> True
"""


from collections import deque


class Stack:
    def __init__(self):
        self.container = deque()

    def push(self, value):
        self.container.append(value)

    def pop(self):
        return None if self.isEmpty() else self.container.pop()

    def peek(self):
        return self.container[-1]

    def size(self):
        return len(self.container)

    def isEmpty(self):
        return True if self.size() == 0 else False


def is_balanced(text):
    s = Stack()
    closingData = {"{": "}", "(": ")", "[": "]"}
    for char in text:
        if char in ["{", "(", "["]:
            s.push(char)
        elif char in ["}", ")", "]"]:
            if char != closingData.get(s.pop(), None):
                return False
    return True


print(is_balanced("({a+b})"))
print(is_balanced("))((a+b}{"))
print(is_balanced("((a+b))"))
print(is_balanced("))"))
print(is_balanced("[a+b]*(x+2y)*{gg+kk}"))
