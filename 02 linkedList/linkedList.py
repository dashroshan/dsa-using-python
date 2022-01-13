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
    ll.insertAtBeginning(1)
    ll.print()
