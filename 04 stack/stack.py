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


if __name__ == "__main__":
    s = Stack()
    s.push(1)
    s.push(2)
    print(s.peek())
    print(s.size())
    s.pop()
    print(s.size())
