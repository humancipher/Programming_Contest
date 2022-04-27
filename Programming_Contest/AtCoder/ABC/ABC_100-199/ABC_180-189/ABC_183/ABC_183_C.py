from itertools import permutations

n,k = map(int,input().split())
T = [list(map(int,input().split())) for _ in range(n)]
P = list(permutations([i for i in range(n)]))

ans = 0
for p in P:
    dist = 0
    if p[0] != 0:
        continue
    for i in range(n):
        dist += T[p[i%n]][p[(i+1)%n]]
    if dist == k:
        ans += 1
print(ans)
