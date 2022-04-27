INF = 10**9

n = int(input())
A = list(map(int,input().split()))

ans = INF
for i in range(-100,101):
    tmp = 0
    for j in range(n):
        tmp += (i-A[j])**2
    ans = min(ans,tmp)
print(ans)