n = int(input())
XY = set()
for _ in range(n):
    x,y = map(int,input().split())
    XY.add((x,y))

ans = 0
for (x0,y0) in XY:
    for (x1,y1) in XY:
        if x0 != x1 and y0 != y1:
            if (x0,y1) in XY and (x1,y0) in XY:
                ans += 1
print(ans//4)