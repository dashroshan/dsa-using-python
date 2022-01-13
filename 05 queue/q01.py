"""
Design a food ordering system where your python program will run two threads,

Place Order: This thread will be placing an order and inserting that into a
queue. This thread places new order every 0.5 second. (hint: use time.sleep(0.5)
function) Serve Order: This thread will server the order. All you need to do is
pop the order out of the queue and print it. This thread serves an order every 2
seconds. Also start this thread 1 second after place order thread is started.
Use this video to get yourself familiar with multithreading in python

Pass following list as an argument to place order thread,

orders = ['pizza','samosa','pasta','biryani','burger'] This problem is a
producer,consumer problem where place_order thread is producing orders whereas
server_order thread is consuming the food orders. Use Queue class implemented in
a video tutorial.
"""

from collections import deque
from threading import Thread
from time import sleep


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


orders = ["pizza", "samosa", "pasta", "biryani", "burger"]
q = Queue()


def placeOrder():
    for order in orders:
        q.enqueue(order)
        sleep(0.5)


def serveOrder():
    while not q.isEmpty():
        print(f"Serverd {q.dequeue()}")
        sleep(1)


tPlace = Thread(target=placeOrder)
tSever = Thread(target=serveOrder)
tPlace.start()
sleep(1)
tSever.start()
