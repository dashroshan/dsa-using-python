"""
In LinkedList class that we implemented in our tutorial add following two
methods,

def insert_after_value(self, data_after, data_to_insert): # Search for first
    occurance of data_after value in linked list # Now insert data_to_insert
    after data_after node

def remove_by_value(self, data): # Remove first node that contains data Now make
    following calls,

    ll = LinkedList()
    ll.insert_values(["banana","mango","grapes","orange"])
    ll.print()
    ll.insert_after_value("mango","apple") # insert apple after mango
    ll.print()
    ll.remove_by_value("orange") # remove orange from linked list
    ll.print()
    ll.remove_by_value("figs")
    ll.print()
    ll.remove_by_value("banana")
    ll.remove_by_value("mango")
    ll.remove_by_value("apple")
    ll.remove_by_value("grapes")
    ll.print()
"""


class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None

    def insertAtBeginning(self, data):
        newNode = Node(data, self.head)
        self.head = newNode

    def insertAtEnd(self, data):
        if self.head is None:
            self.head = Node(data, None)
            return

        itr = self.head
        while itr.next:
            itr = itr.next
        itr.next = Node(data, None)

    def createFromList(self, valuesList=[]):
        self.head = None
        for value in valuesList:
            self.insertAtEnd(value)

    def insertAfterValue(self, insertAfter, value):
        itr = self.head
        while itr:
            if itr.data == insertAfter:
                newNode = Node(value, itr.next)
                itr.next = newNode
                return
            itr = itr.next
        print("Value not found!")

    def removeByValue(self, value):
        itr = self.head
        index = 0
        while itr:
            if itr.data == value:
                self.removeAt(index)
                return
            itr = itr.next
            index += 1
        print(f"{value} is not an element of the linked list!")

    def insertAt(self, index, value):
        if index == 0:
            self.insertAtBeginning(value)
        else:
            itr = self.head
            currentIndex = 0
            while itr:
                currentIndex += 1
                if index == currentIndex:
                    nextNode = itr.next
                    itr.next = Node(value, nextNode)
                    return
                else:
                    itr = itr.next
            if index > currentIndex:
                print(f"The linked list has index upto {currentIndex}!")

    def removeAt(self, index):
        if index == 0:
            self.head = self.head.next
        else:
            itr = self.head
            currentIndex = 0
            while itr:
                currentIndex += 1
                if index == currentIndex:
                    nextNode = itr.next.next
                    itr.next = nextNode
                    return
                else:
                    itr = itr.next
            if index > currentIndex:
                print(f"The linked list has index upto {currentIndex}!")

    def length(self):
        count = 0
        iter = self.head
        while iter:
            iter = iter.next
            count += 1
        return count

    def print(self):
        if self.head is None:
            print("Linked list is empty!")
            return

        itr = self.head
        while itr:
            arrow = "-->" if itr.next else ""
            print(f"{itr.data}{arrow}", end="")
            itr = itr.next


if __name__ == "__main__":
    ll = LinkedList()
    ll.createFromList([1, 2, 3, 4, 5])
    ll.insertAfterValue(4, 10)
    ll.removeByValue(2)
    ll.print()
