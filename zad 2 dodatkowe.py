small = 5
big = 6
goal = 18

import math

def build_bridge(small, big, goal):
    for i in range (1, math.ceil(goal/small)):
        if goal % big == 0 or goal % small ==0:
            return True
        else:
            goal = goal - small
    return False

print(build_bridge(small, big, goal))

 