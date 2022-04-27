r,c,k = map(int,input().split())
n = int(input())
T = [0] * r
Y = [0] * c
RCS = set()
for _ in range(n):
    a,b = map(int,input().split())
    T[a-1] += 1
    Y[b-1] += 1
    RCS.add((a-1,b-1))
TR = [0] * (k+1)
YR = [0] * (k+1)
for i in range(r):
    if T[i] <= k:
        TR[T[i]] += 1
for i in range(c):
    if Y[i] <= k:
        YR[Y[i]] += 1
ans = 0
for i in range(k+1):
    ans += (TR[i] * YR[k-i])
for a,b in RCS:
    if T[a]+Y[b] == k:
        ans -= 1
    if T[a]+Y[b] == k+1:
        ans += 1
print(ans)
