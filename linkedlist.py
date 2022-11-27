class Node:
    def __init__(self, data=None, next_=None):
        self.data = data
        self.next = next_


class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data):  # insert at the beginning
        node = Node(data, self.head)
        self.head = node

    def append(self, data):  # append at the end
        if not self.head:
            self.head = Node(data, None)
            return
        element = self.head
        #  interate on while we have something on the next element
        #  it will stop on last node, cause it does not have a node on next
        while element.next:
            element = element.next
        element.next = Node(data, None)

    def insert_elements(self, *args):  # insert multiple elements
        for i in reversed(args):
            self.insert(i)

    def append_elements(self, *args):
        for i in args:
            self.append(i)

    def remove_at(self, index):
        if index < 0 or index > self.get_length():
            raise Exception('Invalid index')
        if index == 0:
            self.head = self.head.next
            return
        count = 0
        element = self.head
        while element.next:
            #  One step before reaching the element need to remove,
            #  link the current node to the next.next
            if count == index - 1:
                element.next = element.next.next
                break
            element = element.next
            count += 1

    def print(self):
        if not self.head:
            print('None')
            return
        element = self.head
        while element:
            print(element.data, end=' => ')
            element = element.next

    def get_length(self):
        length = 0
        element = self.head
        while element:
            element = element.next
            length += 1
        return length


linkedlist = LinkedList()

linkedlist.insert(5)
linkedlist.insert(4)
linkedlist.insert(3)
linkedlist.insert_elements(1, 2)
linkedlist.append(6)
linkedlist.append_elements(7, 8, 9)

linkedlist.remove_at(8)

linkedlist.print()
