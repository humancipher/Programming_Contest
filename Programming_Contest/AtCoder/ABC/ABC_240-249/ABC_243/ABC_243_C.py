n = int(input())
XY = [list(map(int,input().split())) for _ in range(n)]
S = list(input())
DL,DR = dict(),dict()
for i in range(n):
    x,y = XY[i][0],XY[i][1]
    if S[i] == "L":
        if y not in DL:
            DL[y] = x
        else:
            DL[y] = max(DL[y],x)
    else:
        if y not in DR:
            DR[y] = x
        else:
            DR[y] = min(DR[y],x)
ans = "No"
for y in DL:
    if y in DR:
        if DL[y] > DR[y]:
            ans = "Yes"
            break
print(ans)