n,m = map(int,input().split())
C = [0] * n
for _ in range(m):
    a,b = map(int,input().split())
    C[a-1] += 1
    C[a-1] %= 2
    C[b-1] += 1
    C[b-1] %= 2
ans = "YES"
for i in range(n):
    if C[i] == 1:
        ans = "NO"
print(ans)