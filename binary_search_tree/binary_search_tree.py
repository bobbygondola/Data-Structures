"""
Binary search trees are a data structure that enforce an ordering over 
the data they store. That ordering in turn makes it a lot more efficient 
at searching for a particular piece of data in the tree. 

This part of the project comprises two days:
1. Implement the methods `insert`, `contains`, `get_max`, and `for_each`
   on the BSTNode class.
2. Implement the `in_order_print`, `bft_print`, and `dft_print` methods
   on the BSTNode class.
"""

# We dont need 2 different classes
# are we currently only in one node while traversing? so self is the node we are currently using?
class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    """ PSEUDO FOR INSERT """
    # Insert the given value into the tree
    
    # check if empty
    # if empty, put node at root
    # else if new_node < current.value
    #   left.insert value
    # if >=
    #   right.insert value
    
    
    def insert(self, value):
        new_node = BSTNode(value)
        if value < self.value:              # RECURSION BASE TEST #
            if self.left is None:
                self.left = new_node
            else:                                   # RESTART FUNCTION #
                self.left.insert(value)
        else:                               # OTHER RECURSION TEST # if inserted moved down the list
            if self.right is None:           
                self.right = new_node
            else:
                self.right.insert(value)            # RESTART FUNCTION #
                
                
                
    """ PSEUDO FOR CONTAINS/SEARCH """
    # Return True if the tree contains the value
    # False if it does not
    
    # if node is None:
    #   return False
    # if find.value == node.value
    #   return true
    # else 
    #   if find < node.value   
    #       find on left node
    #   else:
    #       find on right node
    
    def contains(self, target):             # also check for empty DS/array :(
        if self.value == target:            # TEST FOR A FOUND TARGET ON EACH ITERATION #
            return True
        if target < self.value:             # RECURSION BASE TEST # for  lower..
            if self.left:                               # IF EXISTS #
                return self.left.contains(target)           # RECURSIVELY CALL PASSING TARGET #
            else:
                return False
        elif target > self.value:           # RECURSION BASE TEST # for higher..
            if self.right:                                 # IF EXISTS #
                return self.right.contains(target)              # RECURSIVELY CALL PASSING TARGET #
            else:
                return False
                    
            
    """ PSEUDO FOR GET_MAX """
    # Return the maximum value found in the tree
    
    # if theres a right:
    #   get max on right (recursively)
    # else: ..IF NO MORE..
    #   return node.value
    
    def get_max(self):
        
        if self.right:                      # RECURSION TEST
            return self.right.get_max()                 # DIGS DEEPER AND RESETS
        else:                               # NO MORE RIGHTS LEFT..AKA DEEPEST
            return self.value                           # RETURN DEEPEST RIGHT SIDE
        
    
    # # iterative
    # # keep a current largest that weve seen so far.
    # # keep current pointer
    #     current = self
    #     while current.right:
    #         current = current.right
    #     return current.value
    
    
    # iterate down the right child of the current node until no more..(max)
    def get_min(self):
        if self.left:
            return self.left.get_min()
        else:
            return self.value
    

    """ PSEUDO FOR FOR_EACH """
    # Call fn on each self found in the tree
    # Call the function `fn` on the value of each node
    # mimicking for each in JS but in a DataStruc
    # recursively calling fn, through the for_each method
    
    def for_each(self, fn):
        fn(self.value)
        if self.left:                       # RECURSION TEST
            self.left.for_each(fn)                  # RETURN EVERY LEFT INVOKED WITH (FN)
        if self.right:                      # RECURSION TEST
            self.right.for_each(fn)                 # RETURN EVERY RIGHT INVOKED WITH (FN)
            


# REVIEW THIS IF YOU WANT TO GET A JOB WORKING WITH ELON MUSK

    """ TOMORROW """
    
    
    """ 
    DEPTH FIRST TRAVERSAL - go deep down one trail, come back up and try a new path, hitting all nodes.
    
    left first -> back up to any right branches
    
    """
    
    from collections import deque
    
    
    
    
    # Part 2 -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        print(self.value)
        if self.left:
            self.left.in_order_print(node)
        if self.right:
            self.right.in_order_print(node)
        else:
            print("Empty Sorry")
        
        
        
    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    """ why does queue work for breadth first traversal 
        what ds allows us to mimmick recusive --------- because recurive nature is FIFO by nature
        
        left to right
        
        """
    def bft_print(self, node):
        # queue
        # while loop that checks size
        #   pointer variable that pdates at the beginning of each loop
        queue = Queue()
        queue.enqueue(self)
        while queue.size > 0:
            current_node = queue.dequeue()
            if current_node.left:
                queue.enqueue(current_node.left)
            if current_node.right:
                queue.enqueue(current_node.right)
            print(current_node.value)



    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        stack = Stack()
        stack.push(self)
        while stack.size > 0:
            current_node = stack.pop()
            if current_node.right:
                stack.push(current_node.right)
            if current_node.left:
                stack.push(current_node.left)
            print(current_node.value)

    # Stretch Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass
