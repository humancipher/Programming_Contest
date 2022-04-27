import math
n = int(input())

class Coordinate:
    def __init__(self,x,y):
        self.x = x
        self.y = y

def Koch(n,p1,p2):
    if n == 0:
        return
    else:
        s = Coordinate(2/3 * p1.x + 1/3 * p2.x, 2/3 * p1.y + 1/3 * p2.y)
        u = Coordinate(1/3 * p1.x + 2/3 * p2.x, 1/3 * p1.y + 2/3 * p2.y)
        t = Coordinate(1/2*(u.x-s.x) - math.sqrt(3)/2*(u.y-s.y) + s.x, math.sqrt(3)/2*(u.x-s.x) + 1/2*(u.y-s.y) + s.y)
        Koch(n-1,p1,s)
        print(str(s.x) +" "+str(s.y))
        Koch(n-1,s,t)
        print(str(t.x) +" "+str(t.y))
        Koch(n-1,t,u)
        print(str(u.x) +" "+str(u.y))
        Koch(n-1,u,p2)

p1 = Coordinate(0,0)
p2 = Coordinate(100,0)
print(str(p1.x) +" "+str(p1.y))
Koch(n,p1,p2)
print(str(p2.x) +" "+str(p2.y))
