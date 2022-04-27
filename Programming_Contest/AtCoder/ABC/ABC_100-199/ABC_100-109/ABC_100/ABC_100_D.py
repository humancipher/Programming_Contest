n,m = map(int,input().split())
ans = 0

V = [(1,1,1),(1,1,-1),(1,-1,1),(1,-1,-1),(-1,1,1),(-1,1,-1),(-1,-1,1),(-1,-1,-1)]
XYZ = [[0] * n for _ in range(8)]
for i in range(n):
    x,y,z = map(int,input().split())
    for j in range(8):
        XYZ[j][i] += x * V[j][0]
        XYZ[j][i] += y * V[j][1]
        XYZ[j][i] += z * V[j][2]

for j in range(8):
    XYZ[j].sort(reverse=True)
    ans = max(ans,sum(XYZ[j][:m]))
print(ans)
