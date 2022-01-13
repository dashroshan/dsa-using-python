from collections import deque


class Queue:
    def __init__(self):
        self.container = deque()

    def enqueue(self, value):
        self.container.appendleft(value)

    def dequeue(self):
        return None if self.isEmpty() else self.container.pop()

    def size(self):
        return len(self.container)

    def isEmpty(self):
        return True if self.size() == 0 else False


if __name__ == "__main__":
    q = Queue()
    q.enqueue(1)
    q.enqueue(2)
    print(q.dequeue())
    print(q.dequeue())
