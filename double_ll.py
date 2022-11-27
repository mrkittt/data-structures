class Node:
    def __init__(self, data, next_, prev):
        self.data = data
        self.next = next_
        self.prev = prev


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert(self, data):  # insert at the beginning
        node = Node(data, self.head, None)
        if not self.head:
            self.tail = node
        self.head = node

    def append(self, data):  # append at the end
        node = Node(data, None, self.tail)
        if not self.head:
            self.head = node
        self.tail = node

    def print(self):
        element = self.head
        while element:
            print(element.data, end=' => ')
            element = element.next
        print()


ll = LinkedList()
ll.insert(5)
ll.insert(4)
ll.insert(3)
ll.print()
