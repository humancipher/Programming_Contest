N,K = map(int,input().split())
h = [int(input()) for _ in range(N)]

INF = 10**9+1

h.sort()
ans = INF

for i in range(N-K+1):
    ans = min(ans,h[i+K-1]-h[i])

print(ans)
