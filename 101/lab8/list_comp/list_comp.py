#Sydney Jaques
#List_Comp
from funcs_objects import *
from objects import *

def distance_all(points):
   return list(map(lambda p: distance(p, Point(0, 0)), points))
   #variable, what to do to it, in list



def are_in_first_quadrant(points):
   return[point for point in points if point.x > 0 and point.y > 0]
