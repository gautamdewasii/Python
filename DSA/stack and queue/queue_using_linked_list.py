""" 
QUEUE USING LINKED LIST 

enqueue() :- o(1)   # insertion at the rear end (last ) 
dequeue() :-  o(1)  # deleting at the front end ( first node)
display() :- o(n)
"""

# for creating node
class Node:
    def __init__(self, data):
        # node value
        self.data = data
        # for pointing to the next node
        self.next = None

# for linking with nodes and enqueue (append),dequeue (pop), display operations
class Queue:
    # for pointing to the front (front) and rear (end)
    def __init__(self):
        self.rear = None  # END NODE
        self.front = None # FIRST NODE

    # inserting node at the end
    def enqueue(self):
        print("\nEnter the value :- ")
        data = int(input())
        new_node = Node(data)  #New node creating
        # no node in queue
        if self.front is None:
            # initializing front to the new node
            self.front = new_node
        else:
            # if queue contains nodes in it
            # defining old rear node's next to the new node
            self.rear.next = new_node
        #updating rear pointer to the new last node
        self.rear = new_node

    # for deletion operations
    def dequeue(self):
        # if queue is empty
        if self.rear is None:
            print("queue IS EMPTY...")
        # if only one node in queue
        elif self.front == self.rear:
            # initializing rear and front to None
            self.front=None
            self.rear=None
        else:
            # if queue contains more then 1 node in it
            temp = self.front
            self.front = temp.next
            temp = None

    # for displaying queue nodes
    def display(self):
        
        # if queue is empty
        if self.rear is None:
            print("queue IS EMPTY")
        else:
            # if queue contains nodes in it
            temp = self.front
            # until temp doesn't equals to None
            while temp:
                print(f"{temp.data}-->", end=" ")
                temp = temp.next
            print(end="\n")


# STARTING POINT :- 
if __name__ == "__main__":
    
    # defining link for queue ( front and rear)
    queue = Queue()
    while True:
        print("NUMBER OF OPERATIONS :- \nAppend Operation (1) \nPop Operation (2) \nDisplay Operation(3) \nExit (4) \nENTER THE NO:- ")
        operation = int(input())
        if operation == 1:
            print("Enqueue (append) Operation")
            queue.enqueue()
        elif operation == 2:
            print("Dequeue (Pop) operation")
            queue.dequeue()
        elif operation == 3:
            print("Display operation :-")
            queue.display()
        else:
            print("Thanks for using it... :)")
            break

