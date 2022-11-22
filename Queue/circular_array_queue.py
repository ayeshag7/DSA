class ArrayQueue:
    def __init__(self, size):
        self.queue = []
        self.front = -1
        self.rear = -1
        self.size = size

    def enqueue(self, data):
        if self.front == 0 and self.rear == self.size - 1 or \
                self.rear == self.front - 1:  # OR self.rear == (self.front - 1) % (self.size - 1)
            print("Queue is full!")
            return

        elif self.front == -1:
            self.front = self.rear = 0
            self.queue[self.rear] = data

        elif self.rear == self.size - 1 and self.front != 0:
            self.rear = 0
            self.queue[self.rear] = data

        else:
            self.rear += 1
            self.queue[self.rear] = data

    def dequeue(self):
        if self.front == -1:
            print("Queue is empty!")
            return -1

        answer = self.queue[self.front]
        self.queue[self.front] = -1

        if self.front == self.rear:
            self.front = self.rear = -1

        elif self.front == self.size - 1:
            self.front = 0

        else:
            self.front += 1

        return answer
