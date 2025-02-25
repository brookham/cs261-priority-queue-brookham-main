# MaxHeap: A binary 'max' heap.
# Implement as many operations as possible with recursion.
# If you can't figure it out recursively, use a loop. (But then refactor
# your implementation into a recursive one!)
# Your implementation should pass the tests in test_max_heap.py.

# IMPLEMENT THIS CLASS THIRD
# What is the time complexity of each operation?

# Name:
# Collaborators:
# Time spent:

class MaxHeap:
    def __init__(self):
        self._data = []

    def _size(self):
        return len(self._data)
    
    def _is_empty(self):
        if self._size() == 0:
            return True
        
    def _last_index(self):
        return self._size() -1
    
    def _value_at(self, index):
        return self._data[index]
    
    def _left_child_index(self, index):
        left = 2 * index + 1
        return left
    
    def _right_child_index(self, index):
        right = 2 * index + 2
        return right

    def _parent_index(self, index):
        parent = (index-1) // 2
        return parent

    def _parent(self, index):
        return self._data[self._parent_index(index)]
    
    def _left_child(self, index):
        if self._left_child_index(index) in range (self._size()):
            return self._data[self._left_child_index(index)]
        else:
            return None

    def _right_child(self, index):
        if self._right_child_index(index) in range (self._size()):
            return self._data[self._right_child_index(index)]
        else:
            return None

    def _has_left_child(self, index):
        if self._left_child(index):
            return True

    def _has_right_child(self, index):
        if self._right_child(index):
            return True
        
    def _greater_child_index(self, index):
        if not self._has_right_child(index) and not self._has_left_child(index):
            return None
        elif self._has_left_child(index) and not self._has_right_child(index):
            return self._left_child_index(index)
        elif self._has_left_child(index) or self._has_right_child(index):
            if self._left_child(index) >= self._right_child(index):
                return self._left_child_index(index)
            elif self._right_child(index) >= self._left_child(index):
                return self._right_child_index(index)