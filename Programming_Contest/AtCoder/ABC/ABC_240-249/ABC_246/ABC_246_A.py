DX,DY = dict(),dict()
for _ in range(3):
    x,y = map(int,input().split())
    if x not in DX:
        DX[x] = 1
    else:
        DX[x] += 1
    if y not in DY:
        DY[y] = 1
    else:
        DY[y] += 1
Ans = [0,0]
for x in DX:
    if DX[x] == 1:
        Ans[0] = x
for y in DY:
    if DY[y] == 1:
        Ans[1] = y
print(" ".join(map(str,Ans)))