from operator import *
import sys
sys.setrecursionlimit(10100)
import timeit
import random
#import array_list
import linked_list
from linked_list import *
#from array_list import *




#A Catalog is:
# - int
# - string
# - string
# - string
#A Catalog shows a song's number, title, artist, and album
class Catalog:
    def __init__(self, num, title, artist, album):
        self.num = num
        self.title = title
        self.artist = artist
        self.album = album
    def __repr__(self):
        return 'Catalog({}, {}, {}, {})'.format(self.num, self.title, self.artist, self.album)
    def __eq__(self, other):
        return (type(other) == Catalog and self.num == other.num and self.title == other.title and self.artist == other.artist and self.album == other.album)



# ---- functions! ----

#file --> list
#returns a list with the lines which contain errors
def check_for_file_errors(inFile):
    line = 1
    errors = []
    for each in inFile.readlines():
        new = each.rstrip().split('--')
        if len(new) != 3 and new !=['']:
            errors.append(line)
        line += 1
    inFile.close()
    return errors

#song, order --> string
#print the list of songs in the pre-determined order
def print_catalog(song, order):
    if song != None:
        print('{}--{}--{}--{}'.format(song.num, song.title, song.artist, song.album))



#object1 object2 --> bool
#returns true if 1 is larger, false if 2 is larger (calls other comparison functions if ==)
#this is the same for the following sort_new functions:

#returns smallest of song number
def sort_new_num(x, y):
    if x.num < y.num:
        return True
    elif x.num > y.num:
        return False

#returns smallest of title, if same returns smallest of artist, album, num
def sort_new_title(x, y):
    if x.title < y.title:
        return True
    elif x.title > y.title:
        return False
    else:                           #artist
        if x.artist < y.artist:
            return True
        elif x.artist > y.artist:
            return False
        else:
            if x.album < y.album:
                return True
            elif x.album > y.album:
                return False
            else:
                return sort_new_num(x, y)

#returns smallest of artist, if same returns smallest of album, title, num
def sort_new_artist(x, y):
    if x.artist < y.artist:
        return True
    elif x.artist > y.artist:
        return False
    else:                           #album
        if x.album < y.album:
            return True
        elif x.album > y.album:
            return False
        else:
            if x.title < y.title:
                return True
            elif x. title > y.title:
                return False
            else:
                return sort_new_num(x, y)


#returns smallest of album, if same returns smallest of artist, title, num
def sort_new_album(x, y):
    if x.album < y.album:
        return True
    elif x.album > y.album:
        return False
    else:                           #artist
        if x.artist < y.artist:
            return True
        elif x.artist > y.artist:
            return False
        else:
            if x.title < y.title:
                return True
            elif x.title > y.title:
                return False
            else:
                return sort_new_num(x, y)



'''
# -------- Empirical Study ---------
# print out the timing results
def print_timing(desc, iterations, seconds):
   print('{}'.format(seconds))
 
 
# build a list for this test ... the type of list is passed as module
def build_list(n, module, max=10000):
   list = module.empty_list()
   for pos in range(n):
      list = module.add(list, pos, random.randrange(max))
 
   return list
 
 
# the function passed to foreach must take an argument, but we
# don't really want to do anything with it for this experiment
def noop(value, num=0):
   pass

def func(x, y):
    return x < y

# timeit expects that the function passed will take no arguments, so
# this function gathers the arguments and returns a new function that
# uses them, but that itself does not take any arguments
def build_operation(list):
   def run_foreach():
      linked_list.foreach(list, 0, noop)
 
   return run_foreach


def build_operation(list):
    def run_add():
        linked_list.add(list, random.randint(length(list)-1), 5) 
    return run_add


def run_one_experiment(num_elements, num_iterations, module):
   #list = build_list(num_elements, module)
   to_run = build_list(num_elements, module)
   seconds = timeit.timeit(to_run, number=num_iterations)
 
   print_timing('{}'.format(num_elements), num_iterations, seconds)
 
 
def main():


# let's try just one experiment for now
#call run one for each in giant ass array
    for i in range(100, 10000, 200):
        run_one_experiment(i, 1, linked_list)

'''













# ---- Main ----
def main():
    filename = sys.argv[1]
    filename = str(filename)

    try:
        inFile = open(filename, 'r')
    except:
        print('\n{}: No such file or directory\n'.format(filename))
        filename = str(input())
        
    #inFile = inFile.read()
    #inFile = open(filename, 'r')
    mainlist = empty_list()
    counter = 0
    sort_by = 0



    line_errors = check_for_file_errors(inFile)
    if line_errors != []:
        #print error statement
        print('\nCatalog input errors:')
        for line_num in line_errors:
            print('line ' + str(line_num) + ': malformed song information')
        quit()

#making the lists
    inFile = open(filename, 'r')
    for song in inFile:
        music = song.rstrip().split('--')
        if music != ['']:
            title = music[0]
            artist = music[1]
            album = music[2]
            catalog = Catalog(int(counter), title, artist, album)
            if catalog != None:
                mainlist = add(mainlist, counter, catalog)
            counter += 1



#print(main)

    by = None
    answer = 1
    
    while answer != 0:
        print('\nSong Catalog\n   1) Print Catalog\n   2) Song Information\n   3) Sort\n   4) Add Songs\n   0) Quit')
        answer = str(input('Enter Selection: '))
        while answer != '1' and answer != '2' and answer != '3' and answer != '4' and answer != '0':
            print('\nInvalid option')
            print('\nSong Catalog\n   1) Print Catalog\n   2) Song Information\n   3) Sort\n   4) Add Songs\n   0) Quit')
            answer = str(input('Enter Selection: '))
        answer = int(answer)


# ---- Selection 1 ----
#Print Catalog
        if answer == 1:

            if by == 0 or by == None:
                comparison = sort_new_num
            elif by == 1:
                comparison = sort_new_title
            elif by == 2:
                comparison = sort_new_artist
            elif by == 3:
                comparison = sort_new_album

            mainlist = sort(mainlist, comparison)

            order = 0
            foreach(mainlist, order, print_catalog)

# ---- Selection 2 ----
# Song Information
        if answer == 2:
            song_number = input('Enter song number: ')
            if int(song_number) > (length(mainlist) - 1):
                print('\n... Invalid song number')
            else:
                temp = mainlist
                comparison = sort_new_num
                temp = sort(temp, comparison)
                song = get(temp, int(song_number))
                print('\nSong information ...')
                print('   Number: {}'.format(song_number))
                print('   Title: {}'.format(song.title))
                print('   Artist: {}'.format(song.artist))
                print('   Album: {}'.format(song.album))


# ---- Selection 3 ----
#Sort
        if answer == 3:
            print('\nSort songs\n   0) By Number\n   1) By Title\n   2) By Artist\n   3) By Album')
            by = input('Sort by: ')

            #error message
            if by != '0' and by != '1' and by != '2' and by != '3':
                print('\n... Invalid sort option')
        

            else:
            #comparison goes here
                by = int(by)

                if by == 0:
                    comparison = sort_new_num

                if by == 1:
                    comparison = sort_new_title

                if by == 2:
                    comparison = sort_new_artist

                if by == 3:
                    comparison = sort_new_album

                main = sort(mainlist, comparison)

# ---- Selection 4 ----
#Add Songs
        if answer == 4:
            new = input('Enter name of file to load: ')
            error = 0
            try:
                newinfile = open(new, 'r')
            except FileNotFoundError:
                print('\n{}: No such file or directory'.format(new))
                error = 5
            
            #print('\nSong Catalog\n   1) Print Catalog\n   2)   Song Information\n   3) Sort\n   4) Add Songs\n   0) Quit')
            #answer = str(input('Enter Selection: '))
            

            if error != 5:
                newfilename = str(new)
                newinfile = open(newfilename, 'r')



         #newcounter = 1
                for song in newinfile:
                    music = song.rstrip().split('--')
                    if music !=['']:
                        title = music[0]
                        artist = music[1]
                        album = music[2]
                        catalog = Catalog(int(counter), title, artist, album)
                        if catalog != None:
                            mainlist = add(mainlist, counter, catalog)
                        counter += 1

                if by == 1:
                    comparison = sort_new_title
                elif by == 2:
                    comparison = sort_new_artist
                elif by == 3:
                    comparison = sort_new_album
                else:
                    comparison = sort_new_num

                main = sort(mainlist, comparison)
            
           # new_songs = read_from_new_file(newinfile, line_number)
                new_errors = check_for_file_errors(newinfile)
                while new_errors != []:
                    print('\nCatalog input errors')
                    for line in new_errors:
                        print('line ' + str(line) + ': malformed song information')
                        line_number += 1
                    quit()
  

if __name__ == '__main__':
    main()
