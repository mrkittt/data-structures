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
            self.head = node
            self.tail = node
            return
        self.head = node
        node.next.prev = node

    def append(self, data):  # append at the end
        node = Node(data, None, self.tail)
        if not self.head:
            self.head = node
        self.tail = node

    def print_forwards(self):
        element = self.head
        while element:
            print(element.data, end=' => ')
            element = element.next
        print()

    def print_backwards(self):
        element = self.tail
        while element:
            print(element.data, end=' <= ')
            element = element.prev
        print()


ll = LinkedList()
ll.insert(5)
ll.insert(4)
ll.insert(3)
ll.append(6)
ll.append(7)
ll.print_backwards()
