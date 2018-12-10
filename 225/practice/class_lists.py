#Practice with making lists through classes

class NumList:
    def __init__(self, first, rest):
        self.first = first
        self.rest = rest

    def __eq__(self, other):
        return self.first == other.first and self.rest == other.rest

    def __repr__(self, first, rest):
        return('NumList: {}, {}'.format(self.first, self.rest))


#A NumList is one of
# - 'mt'
# - NumList

# ---- Write a Function that returns True if 'dog' is somewhere in the list ----

def contains_dog(NumList):
    if 'mt':
        return False
    else:
        return 
