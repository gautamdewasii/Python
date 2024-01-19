from collections import deque 


"""" 
STACK IMPLEMENTATION USING deque() object:-
deque class importing from collections module

*) Approach is based on LIFO (LAST IN FIRST OUT)
*) Last inserted element place called TOP
*) PUSH OPERATION :- push()
* ) POP OPERATION :- pop()

NOTE :- DEQUE CONSIDERED FASTER THEN list()
"""
## time complexity :-
#1) append() - > o(1)        # added elements at the end of list
#2) pop(-1)  - > o(1)          # only when deleting at the end


def push():  # insertion
    print("\nEnter the value:- ")
    value = int(input())
    stack.append(value)

def pop():
    if len(stack) == 0:
        print("EMPTY STACK...")
    else:
        print("Deleting the last inserted element from the stack ( top element )...")
        stack.pop()

def display():
    if len(stack) == 0:
        print("EMPTY STACK...")
    else:
        for elements in stack:
            print(f"{elements}-->",end=" ")


# STARTING POINT :- 
if __name__ == "__main__":
    
    # defining deque object
    stack = deque()
    while True:
        print("NUMBER OF OPERATIONS :- \nAppend Operation (1) \nPop Operation (2) \nDisplay Operation(3) \nExit (4) \nENTER THE NO:- ")
        operation = int(input())
        if operation == 1:
            print("Append Operation")
            push()
        elif operation == 2:
            print("Pop operation")
            pop()
        elif operation == 3:
            print("Display operation :-")
            display()
        else:
            print("Thanks for using it... :)")
            break

