# print("=============================================\n")
# print("===============CLASS EXAMPLE=================\n")
# # good class
# class Dog:
#     def __init__(self, name, status, cuteness = 0):
#         self.name = name
#         self.status = status
#         self.cuteness = cuteness
        
#     def __str__(self):
#         return f"Name: {self.name}, Status: {self.status}, Cuteness: {self.cuteness}"

# dogs = {
#     "toby": Dog("toby", "good", 10),
#     "crumbs": Dog("crumbs", "good", 11),
#     "cobo": Dog("cobo", "good", 10)
    
# }

# print(dogs["crumbs"])


# print("\n\n")
# print("==============================================\n")
# print("============CONSTANT EXAMPLE==================\n")



# # constant rtc
# # doesnt depend on the size of input/elements/list size
# commands = ['n', 's', 'e', 'w']
# print(commands[0])



# print("\n\n")
# print("===============================================\n")
# print("============QUADRATIC EXAMPLE==================\n")


# # quadratic 
# # print out every combo of pairs of commands
# for counter, x in enumerate(commands):
#     for y in commands:
#         print(counter, x, y)

# print("\n\n")
# print("===============================================\n")
# print("============ENEUMERATE EXAMPLE==================\n")

# # enumerate

# my_list = ["one", "two", "three", "four", "five", "six"]

# for counter, x in enumerate(my_list):         # also u can use key!
#     print(counter, x)
    
print("\n\n")
print("===============================================\n")
print("============Linked List EXAMPLE==================\n")




# before using consise syntax
# ll = Node(1)
# ll.set_next(Node(2))
# ll.next.set_next(Node(3))
#-- old examples..
# ll.next.next.next = Node(4)
# ll.next.next.next.next = Node(4)

# Better Method
# STEP[1] -  create node, 
# STEP[2] - set the old tail to point to new node 
# STEP[3]- reassign tail to refer to the new node

# setup the node class
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
    
    def get_value(self):
        return self.value
    
    def get_next(self):
        return self.next

    def set_next(self, new_next):
        self.next = new_next

# setup the LinkedList class
class LinkedList:
    def __init__(self, head, tail):
        self.head = None
        self.tail = None
    
    def add_to_tail(self, value):
        #create node
        new_node = Node(value)
        if self.tail is None and self.tail is None:
            # set the new node to be the tail
            self.head = new_node
            self.tail = new_node
        else:
            # These 3 steps assume that the tail refers to a node...
            # set old tail's next to refer to new node
            self.tail.set_next(new_node)
            # reassign self.tail to refer to new node
            self.tail = new_node

    def remove_tail(self):
        
        # if we have a non-empty linked list..
        # - iterate over LikedList
        current = self.head
        
        while current.get_next() is not self.tail:
            current = current.get_next
        #at this point, current is the node behind the tail
        
        # set the tail to be None
        val = self.tail.get_value()
        self.tail = None
        # move self.tail to the Node right before
        self.tail = current
        return val
    
    def remove_head(self):
        # check if we have an empty LinkedList
        if self.head is None and self.tail is None:
            return
        
        #what if wehave a single ele linkedList
        if not self.head.get_next():
            head = self.head
            #delete the Linked List head reference
            self.head = None
            self.tail = None
            return head.get_value()
        
        val = self.head.get_value()
        #set self.head to the Node aftet he head
        self.head = self.ehad.get_next()
        return val
        
        
        
         