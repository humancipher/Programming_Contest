x1,y1,x2,y2 = map(int,input().split())
P1,P2 = set(),set()
V = [(1,2),(2,1),(-1,2),(-2,1),(1,-2),(2,-1),(-1,-2),(-2,-1)]
for vx,vy in V:
    P1.add((x1+vx,y1+vy))
    P2.add((x2+vx,y2+vy))
ans = "No"
for x,y in P1:
    if (x,y) in P2:
        ans = "Yes"
        break
print(ans)