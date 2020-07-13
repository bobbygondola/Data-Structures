"""
A stack is a data structure whose primary purpose is to store and
return elements in Last In First Out order. 

1. Implement the Stack class using an array as the underlying storage structure.
   Make sure the Stack tests pass.
2. Re-implement the Stack class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Stack tests pass.
3. What is the difference between using an array vs. a linked list when 
   implementing a Stack?
"""

# set it up with an array for storage

# pancakes
# plates

class Stack:
    def __init__(self, storage = []):
        self.size = 0
        self.storage = storage

    def __len__(self):
        return self.size

    def push(self, value):
        # we push to the top of the storage array
        # push o head, pop from head etc
        pass

    def pop(self):
        pass
