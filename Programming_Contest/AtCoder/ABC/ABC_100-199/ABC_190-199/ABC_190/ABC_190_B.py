N,S,D = map(int,input().split())
XY = [list(map(int,input().split())) for _ in range(N)]

ans = False
for x,y in XY:
    if x < S and y > D:
        ans = True
        break

if ans:
    print("Yes")
else:
    print("No")
