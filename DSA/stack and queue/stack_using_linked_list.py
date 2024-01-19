""" 
STACK USING LINKED LIST 

push() :- o(1)
pop() :-  o(n)
display() :- o(n)
"""

# for creating node
class Node:
    def __init__(self, data):
        # node value
        self.data = data
        # for pointing to the next node
        self.next = None

# for linking with nodes and append,pop,display operations
class Stack:
    # linked
    def __init__(self):
        self.top = None  # END NODE
        self.head = None # FIRST NODE

    # inserting node at the end
    def push(self):
        print("\nEnter the value :- ")
        data = int(input())
        new_node = Node(data)  #New node creating
        # no node in stack
        if self.head is None:
            # initializing head to the new node
            self.head = new_node
        else:
            # if stack contains nodes in it
            # defining old top node's next to the new node
            self.top.next = new_node
        #updating top pointer to the new last node
        self.top = new_node

    # for deletion operations
    def pop(self):
        # if stack is empty
        if self.top is None:
            print("STACK IS EMPTY...")
        # if only one node in stack
        elif self.head == self.top:
            # initializing top and head to None
            self.head=None
            self.top=None
        else:
            # if stack contains more then 1 node in it
            # for iteration from head to top node pointer
            temp = self.head
            while temp.next != self.top:
                temp = temp.next
            # removing top from stack
            temp.next = None
            #initializing new top
            self.top = temp

    # for displaying stack nodes
    def display(self):
        
        # if stack is empty
        if self.top is None:
            print("STACK IS EMPTY")
        else:
            # if stack contains nodes in it
            temp = self.head
            # until temp doesn't equals to None
            while temp:
                print(f"{temp.data}-->", end=" ")
                temp = temp.next
            print(end="\n")


# STARTING POINT :- 
if __name__ == "__main__":
    
    # defining link for stack ( head and top)
    stack = Stack()
    while True:
        print("NUMBER OF OPERATIONS :- \nAppend Operation (1) \nPop Operation (2) \nDisplay Operation(3) \nExit (4) \nENTER THE NO:- ")
        operation = int(input())
        if operation == 1:
            print("Append Operation")
            stack.push()
        elif operation == 2:
            print("Pop operation")
            stack.pop()
        elif operation == 3:
            print("Display operation :-")
            stack.display()
        else:
            print("Thanks for using it... :)")
            break

