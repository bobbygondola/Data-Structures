"""
A queue is a data structure whose primary purpose is to store and
return elements in First In First Out order. 

1. Implement the Queue class using an array as the underlying storage structure.
   Make sure the Queue tests pass.
2. Re-implement the Queue class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Queue tests pass.
3. What is the difference between using an array vs. a linked list when 
   implementing a Queue?
   
Stretch: What if you could only use instances of your Stack class to implement the Queue?
         What would that look like? How many Stacks would you need? Try it!
"""

# line in store
# add to back
# remove from front

from singly_linked_list import LinkedList

class Queue:
    def __init__(self):
        self.size = 0
        self.storage = LinkedList()
    
    def __len__(self):
        return self.size
    
    def enqueue(self, value):         ### appending to the tail
        self.storage.add_to_tail(value)
        self.size += 1
    
    def dequeue(self):                ### removing from the head
        if self.size > 0:
            removed = self.storage.remove_head()
            self.size -= 1
            return removed
        else:
            return None
        

# CALLING, WILL ENQUEUE AND DEQUEUE TO WORK LIKE A REVOLING DOOR/LINE

# class Queue:
    
#     def __init__(self):
#         self.size = 0
#         self.storage = []
    
#     def __len__(self):
#         return len(self.storage)


#     def enqueue(self, value):       # appending to the back
#         self.storage.append(value)
#         self.size += 1

#     def dequeue(self):              # pop-ing from the front
#         if self.storage == []:
#             return None
#         else:
#             self.size -= 1
#             return self.storage.pop(0)
