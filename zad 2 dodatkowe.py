small = 3
big = 5
goal = 8

def build_bridge(small, big, goal):
    for i in range (1, round(goal/small)):
        print(goal/big)
        print (goal%big)
        if goal % big == 0 or goal % small ==0:
            return True
        else:
            goal = goal - small
    return False

print(build_bridge(small, big, goal))

 