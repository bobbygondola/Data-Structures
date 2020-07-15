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
        else:                               # OTHER RECURSION TEST #
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
    
    def contains(self, target):
        if target < self.value:
            if self.left:
                return self.left.contains(target)
            else:
                return False
        elif target > self.value:
            if self.right:
                return self.right.contains(target)
            else:
                return False
        else:
            return True
                    
            
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


    """ PSEUDO FOR FOR_EACH """
    # Call fn on each self found in the tree
    # Call the function `fn` on the value of each node
    # mimicking for each but on different DS
    # recursively calling fn through the for_each fn
    
    def for_each(self, fn):
        fn(self.value)
        if self.left:                       # RECURSION TEST
            self.left.for_each(fn)                  # RETURN EVERY LEFT INVOKED WITH (FN)
        if self.right:                      # RECURSION TEST
            self.right.for_each(fn)                 # RETURN EVERY RIGHT INVOKED WITH (FN)
            

    """ TOMORROW """
    # Part 2 -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        pass

    # Stretch Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass
