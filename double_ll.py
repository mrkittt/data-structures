class Node:
    def __init__(self, data, next_, prev):
        self.data = data
        self.next = next_
        self.prev = prev


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert(self, data):
        self.head = Node(data, self.head, None)
        if not self.head.next:
            self.tail = self.head
        else:
            self.head.next.prev = self.head

    def append(self, data):
        self.tail = Node(data, None, self.tail)
        if not self.tail.prev:
            self.head = self.tail
        else:
            self.tail.prev.next = self.tail

    def print(self):
        element = self.head
        while element:
            print(element.data, end=' -> ')
            element = element.next
        print()

    def print_backwards(self):
        element = self.tail
        while element:
            print(element.data, end=' <- ')
            element = element.prev
        print()
