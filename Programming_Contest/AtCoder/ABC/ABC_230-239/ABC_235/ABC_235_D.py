from collections import deque

INF = 10**10
lim = 10**7-1

a,n = map(int,input().split())
Q = deque()
Q.append([1,0])
D = set()
ans = INF
while len(Q) > 0:
    x,cnt = Q.popleft()
    D.add(x)
    if x == n:
        ans = min(ans,cnt)
    else:
        if x*a not in D and x*a <= lim:
            Q.append([x*a,cnt+1])
            D.add(x*a)
        if x > 10 and x % 10 != 0:
            x2 = str(x)
            x2 = x2[-1] + x2[:len(x2)-1]
            if int(x2) not in D:
                Q.append([int(x2),cnt+1])
                D.add(int(x2))
if ans != INF:
    print(ans)
else:
    print(-1)