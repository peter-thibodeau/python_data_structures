from collections import deque

class DequeQueue:
    def __init__(self):
        self.queue = deque()

    def enqueue(self, item):
        self.queue.append(item) # add item to end of queue

    def dequeue(self):
        if not self.is_empty(): # call is_empty method
            return self.queue.popleft() # return first item in queue
        else:
            return "Queue is empty"

    def is_empty(self): # see if queue is empty
        return len(self.queue) == 0


    def size(self):
        return len(self.queue)  # return size of queue

# create an instance of DequeQueue
q = DequeQueue()

# add some items to the instance of DequeQueue
q.enqueue(10)
q.enqueue(20)
q.enqueue(30)

# test cases
print(f"The first item from the queue is {q.dequeue()}")
print(f"Is the queue empty? {q.is_empty()}")
print(f"Number of items remaining in the queue is {q.size()}\n")

print(f"The next item from the queue is {q.dequeue()}")
print(f"Is the queue empty? {q.is_empty()}")
print(f"Number of items remaining in the queue is {q.size()}\n")

print(f"The next item from the queue is {q.dequeue()}")
print(f"Is the queue empty? {q.is_empty()}")
print(f"Number of items remaining in the queue is {q.size()}")
