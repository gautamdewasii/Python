from collections import deque

"""" 
QUEUE IMPLEMENTATION USING deque() :-
*) Approach is based on FIFO (FIRST IN FIRST OUT)
*) LAST INSERTED ELEMENT CALLED "REAR"
*) FIRST ELEMENT CALLED "FRONT"
*) ENQUEUE OPERATION :-  inserting element at the end , enqueue()
* ) DEQUEUE OPERATION :- deleting element from the "FRONT" ( first element), dequeue()

"""
## time complexity :-
#1) enqueue() - > o(1)        # added elements at the end of list
#2) dequeue(0)  - > o(1)          # only when deleting from the front ( first element)


def enqueue():  # insertion at end of list
    print("\nEnter the value:- ")
    value = int(input())
    queue.append(value)

def dequeue():
    if len(queue) == 0:
        print("EMPTY QUEUE...")
    else:
        print("Deleting the element from FRONT ( first element)")
        queue.popleft()  # o(1) :- deque popleft() optimize to pop left element at constant time

def display():
    if len(queue) == 0:
        print("EMPTY QUEUE...")
    else:
        for elements in queue:
            print(f"{elements}-->",end=" ")


# STARTING POINT :- 
if __name__ == "__main__":
    
    queue = deque()
    while True:
        print("\nNUMBER OF OPERATIONS :- \nAppend Operation (1) \nPop Operation (2) \nDisplay Operation(3) \nExit (4) \nENTER THE NO:- ")
        operation = int(input())
        if operation == 1:
            print("ENQUEUE ( Append) Operation")
            enqueue()
        elif operation == 2:
            print("DEQUEUE ( POP) operation")
            dequeue()
        elif operation == 3:
            print("Display operation :-")
            display()
        else:
            print("Thanks for using it... :)")
            break

