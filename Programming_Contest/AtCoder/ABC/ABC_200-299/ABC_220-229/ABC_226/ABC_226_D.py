from math import gcd

n = int(input())
XY = set([tuple(map(int,input().split())) for _ in range(n)])
Ans = set()
for x1,y1 in XY:
    for x2,y2 in XY:
        dx,dy = x1-x2,y1-y2
        if dx != 0 and dy != 0:
            g = gcd(dx,dy)
        else:
            g = max(abs(dx),abs(dy))
            if g == 0:
                g = 1
        dx //= g
        dy //= g
        Ans.add((dx,dy))
print(len(Ans)-1) #(0,0)以外