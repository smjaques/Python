#  Sydney Jaques
#  Project 3 - Huffman

import string
import inspect
from huffman_bits_io import *
import array_list
import linked_list
import unittest
import os



#textfile --> list
#counts the frequency of occurrences and the index of the character from ASCII and returns it in a list
def count_occurrences(textfile):
    #inFile = HuffmanBitsReader(textfile)
    try:
        inFile = open(textfile, 'r')
    except:
        print('File Not Found')
        exit()

    #inFile = inFile.readlines()
    #the ASCII index is what character it is
    frequency = array_list.empty_list()
    frequency = ([None] * 256)
    #char = string.printable #a list of ascII
    for line in inFile:
        for letter in line: #line.rstrip():
            index = ord(letter)
            if frequency[index] == None:
                frequency[index] = 0
            frequency[index] += 1

    inFile.close()

    '''
    for letter in char:
        if letter != '\n':
            count = count_letter(inFile, letter)
            (character, freq) = (letter, count)
            if freq > 0:
                frequency[ord(character)] = freq
    '''
    return frequency

def count_letter(word, char):
    count = 0
    for c in word:
        if char == c:
            count += 1
    return count




#A HuffmanTree is one of:
# - Leaf(character, frequency, huffmantree)
# - Node(frequency, character, left, right)

#the ends of the tree
class Leaf:
    def __init__(self, frequency, character):
        self.character = character
        self.frequency = frequency
    def __repr__(self):
        return 'Leaf({}, {})'.format(self.frequency, self.character)
    def __eq__(self, other):
        return (type(other) == Leaf and self.character == other.character and self.frequency == other.frequency)

#the nodes of the tree with leaves(left and/or right)
class Node:
    def __init__(self, frequency, character, left, right):
        self.character = character
        self.frequency = frequency
        self.left = left
        self.right = right
    def __repr__(self):
        return 'Node({}, {}, {}, {})'.format(self.frequency, self.character, self.left, self.right)
    def __eq__(self, other):
        return (type(other) == Node and self.frequency == other.frequency and self.character == other.character and self.left == other.left and self.right == other.right)

#An example of a HuffmanTree is: HuffmanNode(10, 'a', HuffmanLeaf('a', 4), HuffmanLeaf('b', 6))




#HuffmanTree --> string
#creates a string from a HuffmanTree by traversing the tree in a pre-order traversal and appending the characters of the visited leaf nodes
def traverse(node):
    rep = ''
    if type(node) != type(Leaf('a', 3)):
        rep += traverse(node.left)
        rep += traverse(node.right)
    elif node != None and type(node) == type(Leaf('a', 3)):
        char = str(node.character)
        rep += char
    return rep

#tree1 tree2 --> bool
#returns true if tree1 comes before tree2; this is decided if the occurrence cound of 1 is smaller
def comes_before(a, b):
    if a.frequency != None and b.frequency != None:
        if a.frequency < b.frequency:
            return True
        elif a.frequency > b.frequency:
            return False
        else:
            if a.character != None and b.character != None:
                return a.character < b.character



# ---- Building the huffman tree ----


#ord(char) frequency --> Leaf
#makes a leaf from one value from the occurrence list function
def make_leaf(index, frequency):
    return Leaf(frequency, index)


#list --> list
#creating a sorted list of individual huffman trees consisting of single Leaf nodes for each character and their occurrence counts
#returns new sorted list
def make_sorted_list(occurrence_list):
    sorted_list = linked_list.empty_list()
    for i in range(array_list.length(occurrence_list)):
        if occurrence_list[i] != None:
            leaf = make_leaf(i, occurrence_list[i])
            sorted_list = linked_list.insert_sorted(sorted_list, leaf, comes_before)
    return sorted_list
 



#list --> list
#creating a sorted list of individual huffman trees consisting of single leaf nodes for each character and their occurrence counts
#returns new sorted list
#THIS ONE KEEPS THE CHARACTER VALUE, NOT THE ASCII VALUE 
def make_character_sorted_list(occurrence_list):
    sorted_list = linked_list.empty_list()
    for i in range(array_list.length(occurrence_list)):
        if occurrence_list[i] != None:
            leaf = make_leaf(chr(i), occurrence_list[i])
            sorted_list = linked_list.insert_sorted(sorted_list, leaf, comes_before)
    return sorted_list





#sortedlist --> huffmantree
#takes lowest two frequency leaves, joins them in a node
def join_leaves(sorted_list):
    #whilethere is more than one node in the list
    while linked_list.length(sorted_list) > 1:
        #remove two nodes from beginning of list (lowest frequencies)
        (leaf1, sorted_list) = linked_list.remove(sorted_list, 0)
        (leaf2, sorted_list) = linked_list.remove(sorted_list, 0)
        #create new Node with these two leaves as children, lesser of two on left(leaf1)
        node_frequency = leaf1.frequency + leaf2.frequency
        if leaf1.character < leaf2.character:
            character = leaf1.character
        else:
            character = leaf2.character
        new_node = Node(node_frequency, character, leaf1, leaf2)
        sorted_list = linked_list.insert_sorted(sorted_list, new_node, comes_before)
    return sorted_list
        




#tree list --> string, list
#traverses our huffman tree from the root (0's when we go left, 1's when we go right), adds all into a string and returns that string
def build_character_code(tree, olist, sequence=''):
    if type(tree) != type(Leaf(1, 2)):
        return build_character_code(tree.left, olist, sequence+'0') and build_character_code(tree.right, olist, sequence+'1')
    
    
    if type(tree) == type(Leaf(1, 2)):
        ordc = tree.character
        index = int(ordc)
        #if sequence == '':
        #    sequence = '1'
        olist[index] = sequence
        sequence += ''

    #else:
        #return build_character_code(tree.left, olist, sequence+'0') and build_character_code(tree.right, olist, sequence+'1')
    
    return olist



#list --> int
#given occurrence list and returns the number of unique codes (characters)
def number_of_codes(olist):
    count = 0
    for each in olist:
        if each != None:
            count += 1
    return count


#string1 string2 --> string
#reads text from input file(string1) and compresses the text into output file(string2)
def huffman_encode(input, output):
    final_encoded = ''
    occurrence_list = count_occurrences(input)
    if all (x== None for x in occurrence_list):
        output = HuffmanBitsWriter(output)
        output.write_code('00')
        output.close()
        return

    

    olist = count_occurrences(input)
    sorted_list = make_sorted_list(occurrence_list)
    pairtree = join_leaves(sorted_list)
    tree = pairtree.first
    code = build_character_code(pairtree.first, occurrence_list) 
    #code is the occurrence list with the encoded string for each ascII value/index
    string = open(input, 'r')
    string2 = string.readlines()
    string.close()
    line = 0
    for each in string2:
        #if line != 0:
        #    final_encoded += code[10]
        for letter in each: #r.strip()
            index = ord(letter)
            encoded= code[index]
            #print(encoded)
            encoded = str(encoded)
            final_encoded += encoded
        #line += 1

    output = HuffmanBitsWriter(output) #open file to write in
    #1) The number of codes represented in the Tree as a single 1 byte integer
    code_num = number_of_codes(occurrence_list)
    output.write_byte(code_num)

    #2) Each character c and number of occurrences n as tuple(c, n)
    for i in range(array_list.length(olist)):
        if olist[i] != None:
            output.write_byte(i)
            num = olist[i]
            num = int(num)
            output.write_int(num)

    #3) Sequence of bits as encoded string
    #print(final_encoded)
    for num in final_encoded:
        output.write_code(num)
    #output.write_code(final_encoded)
    output.close()

    #need the traverse string of CHARACTERS not ASCII values
    string_list = make_character_sorted_list(olist)
    string_pairtree = join_leaves(string_list)
    stringtree = string_pairtree.first



    return traverse(stringtree)
    


#string1 string2 --> None
#reads a compressed file (string1) and write it to output text file (string2)
def huffman_decode(input, output):
    read_from = HuffmanBitsReader(input)
    write_to = open(output, 'w')
    number_of_codes = read_from.read_byte()
    times = 0
    occur_list = array_list.empty_list()
    occur_list = ([None] * 256)
    total_characters = 0
    while times < number_of_codes:
        char = read_from.read_byte()
        freq = read_from.read_int()
        total_characters += freq
        times += 1
        occur_list = array_list.set(occur_list, char, freq)
    if total_characters == 0:
        write_to.write('')
        write_to.close()
        read_from.close()
        return
    sorted_list = make_sorted_list(occur_list)
    pairtree = join_leaves(sorted_list)
    tree = pairtree.first
    temp_tree = tree
    #print(total_characters)
    #read bit by bit and get the code
    bit = True
    code = ''
    chars = 0
    #write_to.write('\n')
    while bit == True or bit == False and chars < total_characters:
        bit = read_from.read_bit()

        if type(tree) != type(Leaf(1, 2)):
            if bit == True:
                tree = tree.right
                code += '1'
            elif bit == False:
                tree = tree.left
                code += '0'

        if type(tree) == type(Leaf('a', 2)):
            char = chr(tree.character)
            write_to.write(char)
            tree = temp_tree
            chars += 1
    #print(code)
    #write_to.write('\n')
    write_to.close()
    read_from.close()
        


from linked_list import *
# ------ Tests ------
class TestList(unittest.TestCase):

    def test_01_textfile1(self):
        s = huffman_encode("textfile.txt", "textfile_encoded.bin")
        self.assertEqual(s, "acb")
        # capture errors by running 'diff' on your encoded file
        # with a *known* solution file
        err = os.system("diff textfile_encoded.bin textfile_encoded_soln.bin")
        self.assertEqual(err, 0)
    def test_01_textfile2(self):
        s = huffman_decode('textfile_encoded.bin', 'original.txt')
        self.assertEqual(s, None)
        err = os.system("diff original.txt textfile.txt")
        self.assertEqual(err, 0)


    def test_count_o5(self):
        olist = [None, None, None, None, None, None, None, None, None, None, 1, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, 3, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, 4, 3, 2, 1, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None]
        self.assertEqual(count_occurrences('test.txt'), olist)
        
    def test_count02(self):
        olist = [None, None, None, None, None, None, None, None, None, None, 2, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, 5, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, 1, 1, 1, 5, None, None, 1, 3, 1, None, 1, None, 2, 3, None, None, 2, 4, 4, 1, None, None, None, 2, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None]
        self.assertEqual(count_occurrences('test2.txt'), olist)
        #olist[10] = 1

    def test_count_l(self):
        self.assertEqual(count_letter('letter', 't'), 2)


    def test_leaf(self):
        self.assertEqual(repr(Leaf(3, 'a')), "Leaf(3, a)")
    def test_leaf2(self):
        self.assertEqual(Leaf(3, 3) == Leaf(3, 3), True)
    
    def test_node(self):
        self.assertEqual(repr(Node(3, 1, 0, 2)), 'Node(3, 1, 0, 2)')
    def test_node2(self):
        self.assertEqual(Node(1, 2, 3, 4) == Node(1, 2, 3, 4), True)


    def test_traverse(self):
        self.assertEqual(traverse(Node(10, 'a', Leaf(4, 'b'), Leaf(6, 'c'))), 'bc')


    def test_comesb(self):
        a = Leaf(6, 6)
        b = Leaf(7, 7)
        self.assertEqual(comes_before(a, b), True)
    def test_comesb2(self):
        a = Leaf(6, 'a')
        b = Node(4, 4, None, None)
        self.assertEqual(comes_before(a, b), False)
    def test_comesb3(self):
        a = Node(6, 4, None, None)
        b = Node(4, 2, None, None)
        self.assertEqual(comes_before(a, b), False)
    def test_comesb4(self):
        a = Node(6, 'a', None, None)
        b = Node(6, 'b', None, None)
        self.assertEqual(comes_before(a, b), True)



    def test_makel(self):
        self.assertEqual(make_leaf(4, 6), Leaf(6, 4))



    def test_make_slist(self):
        olist = [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, 3, 2, 1, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None]
        self.assertEqual(make_sorted_list(olist), Pair(Leaf(1, 99), Pair(Leaf(2, 98), Pair(Leaf(3, 97), None))))


    def test_makecslist(self):
        olist = [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, 3, 2, 1, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None]
        self.assertEqual(make_character_sorted_list(olist), Pair(Leaf(1, 'c'), Pair(Leaf(2, 'b'), Pair(Leaf(3, 'a'), None))))




    def test_joinleaves(self):
        list = Pair(Leaf(1, 99), Pair(Leaf(2, 98), Pair(Leaf(3, 97), None)))
        self.assertEqual(join_leaves(list), Pair(Node(6, 97, Leaf(3, 97), Node(3, 98, Leaf(1, 99), Leaf(2, 98))), None))



    def test_code(self):
        olist = [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, 3, 2, 1, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None]
        tree = Node(6, 97, Leaf(3, 97), Node(3, 98, Leaf(1, 99), Leaf(2, 98)))
        self.assertEqual(build_character_code(tree, olist), [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, '0', '11', '10', None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None])




    def test_numcodesc(self):
        olist = [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, '0', '11', '10', None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None]
        self.assertEqual(number_of_codes(olist), 3)

    def test_numberocodes2(self):
        olist = [None, None, None, None, None, None, None, None, None, None, '101000', None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, '00', None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, '100', '101001', '101010', '101011', '1011', '110000', None, '0101', '11001', None, None, '0110', '11010', '110001', '11011', None, None, '01000', '1110', '0111', None, None, '1111', None, '01001', None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None]
        self.assertEqual(number_of_codes(olist), 19)

    
    def test_encode(self):
        self.assertEqual(huffman_encode('test.txt', 'output.bin'), ' b\ndca')
        #final_encoded = '01011001111110010101110010011010101000110000010110011111011101110000101010100111111000000100011001011011110001110011010101001111011010110111010011'
    def test_decodeit(self):
        self.assertEqual(huffman_encode('test.txt', 'output.bin'), ' b\ndca')
        self.assertEqual(huffman_decode('output.bin', 'newtest.txt'), None)
    def test_decode2(self):
        self.assertEqual(huffman_encode('test2.txt', 'output2.bin'), 'jlnryst eu\niobcdh')
        self.assertEqual(huffman_decode('output2.bin', 'newtest2.txt'), None)
        #textfile = open('newtest', 'r')
        #lines = textfile.readlines()
        #self.assertEqual(lines == ['sydney is the coolest\n', 'junior is better'], True)
        #textfile.close()

    def test_encode2(self):
        self.assertEqual(huffman_encode('empty.txt', 'empty.bin'), None)
        self.assertEqual(huffman_decode('empty.bin', 'orig.txt'), None)

    def test_encode3(self):
        self.assertEqual(huffman_encode('as.txt', 'a.bin'), '\na')
        self.assertEqual(huffman_decode('a.bin', 'aout.txt'), None)
    def test_countexcept(self):
        with self.assertRaises(SystemExit):
            count_occurrences('noexisto.txt')

      
if __name__ == '__main__': 
   unittest.main()
