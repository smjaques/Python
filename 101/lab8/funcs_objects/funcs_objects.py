#Sydney Jaques
#Funcs_Objects
import math


def distance(pt1, pt2):
   return math.sqrt((pt1.x - pt2.x)**2 + (pt1.y - pt2.y)**2)

def circles_overlap(circle1, circle2):
   return distance(circle1.center, circle2.center) < circle1.radius + circle2.radius




