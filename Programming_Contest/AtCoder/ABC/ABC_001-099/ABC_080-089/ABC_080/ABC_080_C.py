def hw(x):
    ans = 0
    while x > 0:
        if x % 2 != 0:
            ans += 1
        x //= 2
    return ans

INF = 10**11

n = int(input())
F = []
for _ in range(n):
    f = tuple(map(int,input().split()))
    tmp = 0
    for i in range(10):
        if f[i] == 1:
            tmp += 2**i
    F.append(tmp)

P = [list(map(int,input().split())) for _ in range(n)]
ans = -INF
for b in range(1,2**10):
    tmp = 0
    for i in range(n):
        h = hw(F[i] & b)
        tmp += P[i][h]
    ans = max(ans,tmp)
print(ans)