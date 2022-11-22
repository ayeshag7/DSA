class Node:
    def __init__(self, element, next):
        self.element = element
        self.next = next


class LinkedStack:
    def __init__(self):
        self.head = None
        self.size = 0

    def display_size(self):
        return self.size

    def is_empty(self):
        if self.size == 0:
            return True
        return False

    def push(self, element):
        if self.is_empty():
            new = Node(element, None)
            self.head = new
            self.size += 1
        else:
            new = Node(element, self.head)
            self.head = new
            self.size += 1

    def pop(self):
        if self.is_empty():
            print("Stack is empty!")
            return None
        node = self.head
        self.head = self.head.next
        self.size -= 1
        return node

    def peek(self):
        if self.is_empty():
            print("Stack is empty!")
            return None
        return self.head.element

    def print_stack(self):
        if self.is_empty():
            print("Stack is empty!")
            return None
        else:
            temp = self.head
            while temp is not None:
                print(temp.element, "-> ", end=" ")
                temp = temp.next
            print(" ")

