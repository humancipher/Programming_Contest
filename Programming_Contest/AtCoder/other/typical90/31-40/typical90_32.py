from itertools import permutations

INF = 10**5

n = int(input())
A = [list(map(int,input().split())) for _ in range(n)]
m = int(input())
F = set()
for _ in range(m):
    x,y = map(int,input().split())
    F.add((x-1,y-1))
    F.add((y-1,x-1))

P = list(permutations([i for i in range(n)]))
ans = INF
for junjo in P:
    use = True
    for i in range(n-1):
        if (junjo[i],junjo[i+1]) in F:
            use = False
    if use:
        tmp = 0
        for i in range(n):
            tmp += A[junjo[i]][i]
        ans = min(ans,tmp)
if ans == INF:
    print(-1)
else:
    print(ans)