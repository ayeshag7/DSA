class ArrayQueue:
    def __init__(self, size):
        self.queue = []
        self.front = 0
        self.rear = 0
        self.size = size

    def is_empty(self):
        if self.front == self.rear:
            return True
        return False

    def enqueue(self, data):
        if self.size == self.rear:
            print("Queue is full!")
            return
        else:
            self.queue[self.rear] = data
            self.rear += 1

    def dequeue(self):
        if self.is_empty():
            print("Queue is empty!")
            return
        else:
            answer = self.front
            self.queue[self.front] = -1
            self.front += 1

            if self.front == self.rear:
                self.front = 0
                self.rear = 0

        return answer

    def peek_queue(self):
        if self.front == self.rear:
            print("Queue is empty!")
        else:
            return self.queue[self.front]

    def print_queue(self):

        if self.front == self.rear:
            print("\nQueue is empty")

        for i in self.queue:
            print(i, "<--", end='')
