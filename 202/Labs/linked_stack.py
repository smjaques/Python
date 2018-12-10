#  Sydney Jaques
#  Linked Stack


from linked_list import *
# A stack is one of
# - None
# - Node(int, stack)



#  --> stack
#takes no arguments and returns an empty stack
def empty_stack():
    return None


#stack, value --> stack
#adds the value to the top of the stack
def push(stack, value):
    new_stack = add(stack, 0, value)
    return new_stack

#stack --> tuple
#given a stack it removes the top element
def pop(stack):
    return remove(stack, 0)



#stack --> int
#given a stack it returns the top element
def peek(stack):
    return get(stack, 0)


#stack --> int
#given a stack it returns the number of elements 
def size(stack):
    return length(stack)


#stack --> book
#given a stack it returns a True if the stack is empty (false otherwise)
def is_empty(stack):
    return stack == None
