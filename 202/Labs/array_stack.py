#  Sydney Jaques
#  Array Stack
from array_list import *


#  --> stack
#takes no arguments and returns an empty stack
def empty_stack():
    return empty_list()


#stack value --> stack
#returns a stack with the value added to the top
def push(stack, value):
    return add(stack, 0, value)


#stack --> tuple
#removes the top element in the stack, returns (removed element, rest)
def pop(stack):
    if is_empty(stack) == True:
        raise IndexError
    index = size(stack)
    return remove(stack, 0)

#stack --> int
#returns the top element in the stack
def peek(stack):
    return get(stack, 0)

#stack --> int
#returns the number of elements in the stack
def size(stack):
    return length(stack)

#stack --> bool
#returns true if the stack is empty, false otherwise
def is_empty(stack):
    if stack.size == 0:
        return True
    return False


