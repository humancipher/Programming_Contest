from collections import deque

n = int(input())
P = list(map(int,input().split()))
P2 = [P[n-i-1] for i in range(n)]
P = deque(P)
P2 = deque(P2)
ans = 10**6
for i in range(n):
    if P[0] == 1 and P[n-1] == n:
        ans = min(ans,i)
    if P[0] == n and P[n-1] == 1:
        ans = min(ans,i+1)
    if P2[0] == 1 and P2[n-1] == n:
        ans = min(ans,i+1)
    if P2[0] == n and P2[n-1] == 1:
        ans = min(ans,i+2)
    x = P.popleft()
    P.append(x)
    y = P2.popleft()
    P2.append(y)
print(ans)