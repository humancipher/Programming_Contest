INF = 10**20

n = int(input())
AT = [list(map(int,input().split())) for _ in range(n)]
q = int(input())
X = list(map(int,input().split()))
diff,upper,lower = 0,INF,-INF
for a,t in AT:
    if t == 1:
        diff += a
        upper += a
        lower += a
    if t == 2:
        lower = max(lower,a)
        upper = max(upper,a)
    if t == 3:
        upper = min(upper,a)
        lower = min(lower,a)
Ans = []

for x in X:
    x += diff
    x = min(x,upper)
    x = max(x,lower)
    Ans.append(x)
for i in range(q):
    print(Ans[i])