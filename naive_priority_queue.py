# NaivePriorityQueue (aka 'ShittyQueue'): A simple but inefficient priority queue.
# Your implementation should pass the tests in test_naive_priority_queue.py.

# IMPLEMENT THIS CLASS SECOND.
# What is the time complexity of each operation?

# Name: Brook Hamilton
# Collaborators:
# Time spent:

class NaivePriorityQueue:
    def __init__(self):
        self.data = []
        self.size = 0

    def enqueue(self, value):
        self.data.append(value)
        self.size += 1

    def dequeue(self):
        self.data = sorted(self.data)
        self.size -= 1
        return self.data.pop()
    
    def is_empty(self):
        if self.size == 0:
            return True