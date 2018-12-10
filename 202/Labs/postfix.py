#  Sydney Jaques
#  Postfix

#from linked_stack import *
from array_stack import *

def postfix_calc(string):
    list = string.split()
    stack = empty_stack()
    for i in list:
        if i != '+' and i != '-' and i != '/' and i != '*':
            stack = push(stack, float(i))
        else:
            second_val = pop(stack)[0]
            first_val = pop(stack)[0]
            if i == '+':
                value = first_val + second_val
            elif i == '-':
                value = first_val - second_val
            elif i == '*':
                value = first_val * second_val
            elif i == '/':
                value = first_val / second_val
            stack = push(stack, value)
    return peek(stack)












