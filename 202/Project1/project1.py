# Name: Sydney Jaques
# Project 1

import unittest


    
# ---- 2 ----
# A StrList is one of
# - 'mt'
# - Pair(string, StrList)

class Pair:
    def __init__(self, first, rest):
        self.first = first
        self.rest = rest
    def __repr__(self):
        return 'Pair({}, {})'.format(self.first, self.rest)
       
    def __eq__(self, other):
        return ((type(other) == Pair) and self.first == other.first and self.rest == other.rest)


# ---- 3 ----
# A ClassShape has
# - name
# - StrList of field names

class ClassShape:
    def __init__(self, name, StrList):
        self.name = name
        self.StrList = StrList
    def __repr__(self):
        return 'ClassShape({}, {})'.format(self.name, self.StrList)

    def __eq__(self, other):
        return (type(other) == ClassShape
               and self.name == other.name
               and self.StrList == other.StrList
               )


# ---- 4 ----
#A StrList represents the lines of code in a program
#StrList --> string
#returns a single string with all the lines of code together with a new line at beginning/end
def join_lines(StrList):
    if StrList == 'mt':
        return ''
    else:
        return (StrList.first + '\n' + join_lines(StrList.rest))


# ---- 5 ----
#A field represents a variable in the init function
#field --> init line
#returns the line in the init function with the given field
def single_field_to_assignments(field):
    if field == 'mt':
        return 'mt'
    return ('        self.' + field + ' = ' + field)

#A Strlist represents a list of fields
#Strlist --> init lines
#returns the lines in the init function with the given fields
def fields_to_assignments(StrList):
    if StrList == 'mt':
        return 'mt'
    else:
        return (Pair(single_field_to_assignments(StrList.first), fields_to_assignments(StrList.rest)))


# ---- 6 ----
#A Strlist represents a list of fields
#Strlist --> string
#returns what would be the first line of the init function - each variable separated by comas
def commasep(StrList):
    if StrList == 'mt':
        return ''
    else:
        return (', ' + StrList.first + commasep(StrList.rest))


# ---- 7 ----
#A Strlist represents a list of fields
#Strlist --> Strlist
#returns the lines of an __init__ function
def init_method(StrList):
    if StrList == 'mt':
        return Pair('    def __init__(self):', Pair('        pass', 'mt'))
    else:
        assignments = fields_to_assignments(StrList)
        print(assignments)
        joined = join_lines(assignments)
        print(joined)
        def_init = commasep(StrList)
        return Pair('    def __init__(self' + def_init +'):', Pair(joined, 'mt'))



# ---- 8 ----
#A Strlist represents a list of fields
#Strlist --> Strlist
#returns the lines of an __eq__ function

def field_lines(field):
    if field == 'mt':
        return 'mt'
    return ('                and self.' + field + ' == ' + 'other.' + field)

def fields_lines(StrList):
    if StrList == 'mt':
        return 'mt'
    else:
        return (Pair(field_lines(StrList.first), fields_lines(StrList.rest)))


def eq_method(ClassShape):
    if ClassShape.StrList == 'mt':
        return Pair('    def __eq__(self, other):', Pair('        pass', 'mt'))
    else:
        assignments = fields_lines(ClassShape.StrList)
        joined = join_lines(assignments)
        return Pair('    def __eq__(self, other):', Pair('        return (type(other) == ' + ClassShape.name, Pair(joined + '                )', 'mt')))


# ---- 9 ----
#A Strlist represents a list of fields
#A ClassShape represents 
# - A string
# - A StrList
#The ClassShape is a list of the class name and a StrList with the class fields
#returns the lines of a __repr__ function

def join_repr_lines(StrList):
    if StrList == 'mt':
        return 'mt'
    else:
        return (Pair(repr_line(StrList.first), repr_lines(StrList.rest)))

def repr_line(field):
    if field == 'mt':
        return 'mt'
    else:
        return ('self.' + field)

def repr_lines(StrList):
    if StrList == 'mt':
        return 'mt'
    else:
        return (Pair(repr_line(StrList.first), repr_lines(StrList.rest)))

def repr_method(ClassShape):
    if ClassShape.StrList == 'mt':
        return Pair('    def __repr__(self):', Pair('        pass', 'mt'))
    else:
        lines = join_repr_lines(ClassShape.StrList)
        newtry = lines.first + commasep(lines.rest)
        return Pair('    def __repr__(self):', Pair('        return "' + ClassShape.name + '({!r}, {!r})".format(' + newtry + ')', 'mt'))


# ---- 10 ----
#ClassShape --> string
#returns the entire class definition

def render_class(ClassShape):
    if ClassShape.StrList == 'mt':
        return 'mt'
    else:
        functions = join_lines(init_method(ClassShape.StrList)) + join_lines(eq_method(ClassShape)) + '\n' + join_lines(repr_method(ClassShape))
        return ('class ' + ClassShape.name + ':\n' + functions)







class TestCase(unittest.TestCase):

# ---- init Tests ----
    def test_join_str(self):
        self.assertEqual(join_lines('mt'), '')
    def test_join_str1(self):
        self.assertEqual(join_lines(Pair('Mary', Pair('had', Pair('a', Pair('little', Pair('lamb', 'mt')))))), 'Mary\nhad\na\nlittle\nlamb\n')
    def test_join_str2(self):
        self.assertEqual(join_lines(Pair('what', Pair('is', Pair('up?', 'mt')))), 'what\nis\nup?\n')

    def test_single_field(self):
        self.assertEqual(single_field_to_assignments('first'), '        self.first = first')
    def test_single_field2(self):
        self.assertEqual(single_field_to_assignments('last'), '        self.last = last')
    def test_single_field3(self):
        self.assertEqual(single_field_to_assignments('mt'), 'mt')

    def test_fields(self):
        self.assertEqual(fields_to_assignments(Pair('first', 'mt')), Pair('        self.first = first', 'mt'))
    def test_fields2(self):
        self.assertEqual(fields_to_assignments(Pair('a', Pair('b', Pair('c', 'mt')))), Pair('        self.a = a', Pair('        self.b = b', Pair('        self.c = c', 'mt'))))

    def test_comasep(self):
        self.assertEqual(commasep('mt'), '')
    def test_comasep2(self):
        self.assertEqual(commasep(Pair('abc', Pair('def', 'mt'))), ', abc, def')

    def test_init(self):
        self.assertEqual(init_method(Pair('first', Pair('rest', 'mt'))), Pair('    def __init__(self, first, rest):', Pair('        self.first = first\n        self.rest = rest\n', 'mt')))
    def test_init2(self):
        self.assertEqual(init_method('mt'), Pair('    def __init__(self):', Pair('        pass', 'mt')))



# ---- eq Tests ----
    def test_field_lines(self):
        self.assertEqual(field_lines('mt'), 'mt')
    def test_field_lines2(self):
        self.assertEqual(field_lines('radius'), '                and self.radius == other.radius')

    def test_fields_lines(self):
        self.assertEqual(fields_lines('mt'), 'mt')
    def test_fields_lines2(self):
        self.assertEqual(fields_lines(Pair('yes', Pair('no', 'mt'))), Pair('                and self.yes == other.yes', Pair('                and self.no == other.no', 'mt')))

    def test_eq(self):
        cs = ClassShape('Plate', Pair('diameter', Pair('material', 'mt')))
        self.assertEqual(eq_method(cs), Pair('    def __eq__(self, other):', Pair('        return (type(other) == Plate', Pair('                and self.diameter == other.diameter\n                and self.material == other.material\n                )', 'mt'))))
    def test_eq2(self):
        self.assertEqual(eq_method(ClassShape('Pair', 'mt')), Pair('    def __eq__(self, other):', Pair('        pass', 'mt')))

# ---- repr Tests ----
    def test_join_repr_lines(self):
        self.assertEqual(join_repr_lines('mt'), 'mt')
    def test_join_repr_lines2(self):
        self.assertEqual(join_repr_lines(Pair('hey', Pair('its', Pair('sydney', 'mt')))), Pair('self.hey', Pair('self.its', Pair('self.sydney', 'mt'))))

    def test_repr_line(self):
        self.assertEqual(repr_line('mt'), 'mt')
    def test_repr_line2(self):
        self.assertEqual(repr_line('radius'), 'self.radius')
    
    def test_repr_lines(self):
        self.assertEqual(repr_lines('mt'), 'mt')
    def test_repr_lines2(self):
        self.assertEqual(repr_lines(Pair('radius', Pair('center', 'mt'))), Pair('self.radius', Pair('self.center', 'mt')))

    def test_repr(self):
        self.assertEqual(repr_method(ClassShape('name', 'mt')), Pair('    def __repr__(self):', Pair('        pass', 'mt')))
    def test_repr2(self):
        self.assertEqual(repr_method(ClassShape('name', Pair('field', Pair('field2','mt')))), Pair('    def __repr__(self):', Pair('        return "name({!r}, {!r})".format(self.field, self.field2)', 'mt')))


    def test_repr_func(self):
        self.assertEqual(repr(Pair('field', 'mt')), 'Pair(field, mt)')

    def test_repr_classshape(self):
        self.assertEqual(repr(ClassShape('name', Pair('hey', 'mt'))), 'ClassShape(name, Pair(hey, mt))')

    def test_eq_orig(self):
        self.assertEqual(Pair('hey', 'mt') == Pair('hey', 'mt'), True)
    def test_eq_orig2(self):
        self.assertEqual(Pair('hey', 'mt') == Pair('hey', Pair('syd', 'mt')), False)
    def test_eq_orig3(self):
        self.assertEqual('mt' == 'mt', True)
    def test_eq_orig_class(self):
        self.assertEqual(ClassShape('name', Pair('hey', 'mt')) == ClassShape('name', Pair('hey', 'mt')), True)
    def test_eq_orig_class2(self):
        self.assertEqual(ClassShape('name', 'mt') == ClassShape('name', 'mt'), True)



    def test_render(self):
        self.assertEqual(render_class(ClassShape('name', 'mt')), 'mt')
    def test_render2(self):
        self.assertEqual(render_class(ClassShape('Name', Pair('field', Pair('field2', 'mt')))), 'class Name:\n    def __init__(self, field, field2):\n        self.field = field\n        self.field2 = field2\n\n    def __eq__(self, other):\n        return (type(other) == Name\n                and self.field == other.field\n                and self.field2 == other.field2\n                )\n\n    def __repr__(self):\n        return "Name({!r}, {!r})".format(self.field, self.field2)\n')













if __name__ == '__main__':
    unittest.main()





   # ClassShape(Plate, Pair('diameter', Pair('material', 'mt')))

