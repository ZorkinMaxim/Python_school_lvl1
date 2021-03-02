import math

def findDistance(x1,x2,y1,y2):
    dist = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    return dist

print(findDistance(2,5,3,8))