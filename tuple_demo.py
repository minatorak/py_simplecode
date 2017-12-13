point = 1,7
### point = (1,7)

# print(point)
# print(type(point))
# print(point[0])
# print(point[1])
#
# th = "thailand",5,10,15.4
# print(th)
# print(th[1] + th[2] + th[3])

def distance(pointA,pointB):
    ## sqrt((X1 - X2)^2 + (y1 - y2)^2)
    return ((pointA[0]-pointB[0])**2 + (pointA[1]-pointB[1])**2)**0.5

pointA = 1,7
pointB = 1,10
d = distance(pointA,pointB)
print(d)
