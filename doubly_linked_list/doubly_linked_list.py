


class ListNode:
    def __init__(self, value, prev = None, next = None):
        self.value = value
        self.prev = prev
        self.next = next
    
    def get_value(self):
        return self.value
    
    def set_next(self, new_next):
        self.next = new_next
    
    
    
    """Wrap the given value in a ListNode and insert it
    # after this node. Note that this node could already
    # have a next node it is point to."""
    
    def insert_after(self, value):
        current_next = self.next
        self.next = ListNode(value, self, current_next)
        if current_next:
            current_next.prev = self.next
            
    
    
    """Wrap the given value in a ListNode and insert it
    # before this node. Note that this node could already
    # have a previous node it is point to."""
    
    def insert_before(self, value):
        current_prev = self.prev
        self.prev = ListNode(value, current_prev, self)
        if current_prev:
            current_prev.next = self.prev
            
    
    
    """Rearranges this ListNode's previous and next pointers
    # accordingly, effectively deleting this ListNode."""
    
    def delete(self):
        if self.prev:
            self.prev.next = self.next
        if self.next:
            self.next.prev = self.prev


""" THE DOUBLY-LINKED-LIST CLASS """

class DoublyLinkedList:
    def __init__(self, node = None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0
    
        
    def __len__(self):
        return self.length

    
    """ Adds a new_node instance as the new head of the list. Don't forget to handle 
    the old head node's previous pointer accordingly."""
    
    def add_to_head(self, value):
        # instance
        new_node = ListNode(value, None, None)
        # if empty
        if not self.head and not self.tail:
            self.head = new_node
            self.tail = new_node
            self.length += 1
        else:
            # 1. reassign head ref to new node
            # 2. new head's next, needs to point to the old head!
            # 3. old heds prev, eeds to point to the new head
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
            self.length += 1
    
    
    """Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly."""
    
    def add_to_tail(self, value):
        new_node = ListNode(value)
        self.length += 1
        if not self.head and not self.tail:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
    
    
    """Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node."""
    
    def remove_from_head(self):
        value = self.head.value
        self.delete(self.head)
        return value
    

    """Removes the List's current tail node, making the 
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node."""
    
    def remove_from_tail(self):
        value = self.tail.value
        self.delete(self.tail)
        return value
    
    """Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List."""
    
    def move_to_front(self, node):
        if node is self.head:
            return
        self.add_to_head(node.value)
        self.delete(node)
        
        
    """Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List."""
    
    def move_to_end(self, node):
        if node is self.tail:
            return
        self.add_to_tail(node.value)
        self.delete(node)
    
    
    """Removes a node from the list and handles cases where
    the node was the head or the tail"""
    
    def delete(self, node):
        self.length -= 1
        if self.head is self.tail:
            self.head = None
            self.tail = None
        elif node is self.head:
            self.head = node.next
            node.delete()
        elif node is self.tail:
            self.tail = node.prev
            node.delete()
        else:
            node.delete()
    
    
    """Returns the highest value currently in the list"""
    
    def get_max(self):
        if self.right:                      # RECURSION TEST
            return self.right.get_max()                 # DIGS DEEPER AND RESETS
        else:                               # NO MORE RIGHTS LEFT..AKA DEEPEST
            return self.value                           # RETURN DEEPEST RIGHT SIDE
    
    # def get_min