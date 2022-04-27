N = int(input())
T = [int(input()) for _ in range(N)]

ans = T[0]
for i in range(1,N):
    ans = min(ans,T[i])

print(ans)
