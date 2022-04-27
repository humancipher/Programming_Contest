def judge(XY):
    x1 = XY[1][0]-XY[0][0]
    y1 = XY[1][1]-XY[0][1]
    x2 = XY[2][0]-XY[0][0]
    y2 = XY[2][1]-XY[0][1]
    S = abs(x1*y2 - x2*y1) 
    return S != 0 and S % 2 == 0

n = int(input())
XY = [list(map(int,input().split())) for _ in range(n)]
ans = 0
for i in range(n):
    for j in range(i+1,n):
        for k in range(j+1,n):
            A = [XY[i],XY[j],XY[k]]
            if judge(A):
                ans += 1
print(ans)
