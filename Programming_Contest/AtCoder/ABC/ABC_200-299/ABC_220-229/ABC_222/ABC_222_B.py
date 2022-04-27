n,p = map(int,input().split())
A = list(map(int,input().split()))

ans = 0
for i in range(n):
    if A[i] < p:
        ans += 1
print(ans)