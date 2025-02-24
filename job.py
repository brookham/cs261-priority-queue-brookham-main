# Job: A process or task that has a priority.
# Your implementation should pass the tests in test_job.py.

# IMPLEMENT THIS CLASS FIRST

# Name: Brook Hamilton
# Collaborators:
# Time spent:

class Job:
    def __init__(self, priority=None, message=None):
        self.priority = priority
        self.message = message
    
    def __eq__(self, priority):
        if isinstance(priority, Job):
            if self.priority == priority.priority:
                return True
        return False
    
    def __lt__ (self, priority):
        if self.priority < priority.priority:
            return True




 