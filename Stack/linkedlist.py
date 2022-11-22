class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def add_at_start(self, data):
        new = Node(data)
        new.next = self.head
        self.head = new

    def remove_from_start(self):
        if self.head is not None:
            temp = self.head.next
            self.head.next = None
            self.head = temp
        else:
            return None

    def add_at_end(self, data):
        new = Node(data)
        if self.head is not None:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new
            new.next = None
        else:
            self.head = new

    def remove_from_end(self):
        if self.head is None:
            return None
        elif self.head.next is None:
            self.head = None
        else:
            current = self.head
            while current.next.next is not None:
                current = current.next
            current.next = None

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.data, "-> ", end=" ")
            temp = temp.next
        print(" ")
