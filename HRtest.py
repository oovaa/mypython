



import math
import os
import random
import re
import sys


class Car:
    maxspeed = None
    unit = None
    def __init__(self, maxspeed, unit):
        self.maxspeed = maxspeed
        self.unit = unit
        print('Car with them maximum speed of',str(maxspeed),unit)


class Boat:
 maximumspeed = None
 def __init__(self,maximumspeed):
     self.maximumspeed = maximumspeed
     print('Boat with them maximum speed of',str(maximumspeed),'knots')
     
     
Car1 = Car(120,'km/h')
b1 = Boat(120)


# if __name__ == '__main__':
#     fptr = open(os.environ['OUTPUT_PATH'], 'w')
#     q = int(raw_input())
#     queries = []
#     for _ in xrange(q):
#         args = raw_input().split()
#         vehicle_type, params = args[0], args[1:]
#         if vehicle_type == "car":
#             max_speed, speed_unit = int(params[0]), params[1]
#             vehicle = Car(max_speed, speed_unit)
#         elif vehicle_type == "boat":
#             max_speed = int(params[0])
#             vehicle = Boat(max_speed)
#         else:
#             raise ValueError("invalid vehicle type")
#         fptr.write("%s\n" % vehicle)
#     fptr.close()












# import math
# import os
# import random
# import re
# import sys


# # write your code here
# def avg(*args):
#  sum =0
#  for i in args:
#      sum += i
#      print(args.index(i)+1)
    
#  return sum/len(args)

# print(avg(2,5))
# print(avg(1,2,3,4,5,6,7,8,9,10))
# # print(avg(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35))