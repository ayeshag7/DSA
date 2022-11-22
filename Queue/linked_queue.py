class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedListQueue:

    def __init__(self):
        self.front = None
        self.rear = None

    def is_empty(self):
        return self.front is None

    def enqueue(self, data):
        temp = Node(data)
        if self.rear is None:
            self.front = self.rear = temp
            return
        self.rear.next = temp
        self.rear = temp

    def dequeue(self):
        if self.is_empty():
            print("Queue is empty!")
            return
        temp = self.front
        self.front = temp.next
        if self.front is None:
            self.rear = None

    def peek_queue(self):
        if self.is_empty():
            print("Queue is empty!")
            return
        else:
            return self.front.data

    def size_of_queue(self):
        size = 0
        temp = self.front
        while temp is not None:
            size += 1
            temp = temp.next
        return size

    def print_queue(self):
        temp = self.front
        while temp is not None:
            print(temp.data, "<- ", end=" ")
            temp = temp.next
        print(" ")


q = LinkedListQueue()
q.enqueue(4)
q.enqueue(5)
q.enqueue(6)
q.print_queue()
q.dequeue()
q.print_queue()
