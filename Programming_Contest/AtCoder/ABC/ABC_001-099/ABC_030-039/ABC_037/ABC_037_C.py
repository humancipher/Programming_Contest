N,K = map(int,input().split())
a = list(map(int,input().split()))

for i in range(1,N):
    a[i] += a[i-1]
a = [0] + a

ans = 0
for i in range(K,N+1):
    ans += (a[i] - a[i-K])

print(ans)
