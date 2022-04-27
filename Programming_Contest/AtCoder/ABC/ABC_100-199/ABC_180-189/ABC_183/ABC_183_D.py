from itertools import accumulate

N,W = map(int,input().split())
STP = [list(map(int,input().split())) for _ in range(N)]

t_max = 0
for i in range(N):
    t_max = max(t_max,STP[i][1])

Use = [0 for _ in range(t_max+1)]

for s,t,p in STP:
    Use[s] -= p
    Use[t] += p

Use = list(accumulate(Use))

if min(Use) < -W:
    print("No")
else:
    print("Yes")
