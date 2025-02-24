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

    def enqueue(self, value):
        self.data.append(value)

    def dequeue(self):
        self.data = sorted(self.data)
        return self.data.pop()