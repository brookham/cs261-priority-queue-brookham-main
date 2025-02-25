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
        elif self._has_left_child(index) and self._has_right_child(index):
            if self._left_child(index) >= self._right_child(index):
                return self._left_child_index(index)
            else:
                return self._right_child_index(index)
            
    def _obeys_heap_property_at_index(self, index):
        if not self._has_left_child(index) and not self._has_right_child(index):
            return True
        if self._has_left_child(index) and self._value_at(index) < self._left_child(index):
            return False
        if self._has_right_child(index) and self._value_at(index) < self._right_child(index):
            return False
        return True
    
    def _swap(self, a, b):
        self._data[a], self._data[b] = self._data[b], self._data[a]

    def _sift_down(self, index):
        if not self._has_left_child(index) and not self._has_right_child(index):
            return
        if not self._obeys_heap_property_at_index(index):
            child_index = self._greater_child_index(index)
            self._swap(index, child_index)
            self._sift_down(child_index)

    def _sift_up(self, index):
        if index == 0:
            return
        parent_index = self._parent_index(index)
        if self._value_at(index) > self._value_at(parent_index):
            self._swap(index, parent_index)
            self._sift_up(parent_index)

    def insert(self, value):
        self._data.append(value)
        self._sift_up(self._last_index())

    def delete(self):
        if self._is_empty():
            return None
        self._swap(0, self._last_index())
        deleted = self._data.pop()
        self._sift_down(0)
        return deleted