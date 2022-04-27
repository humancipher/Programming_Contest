r,c,d = map(int,input().split())
A = [list(map(int,input().split())) for _ in range(r)]

ans = 0
for i in range(r):
    for j in range(c):
        if (i+j-d) % 2 == 0 and i+j <= d:
            ans = max(ans,A[i][j])
print(ans)
