n,x = map(int,input().split())
A = list(map(int,input().split()))
A = [0] + A
F = [False] * (n+1)
pt = x
while True:
    if not F[pt]:
        F[pt] = True
        pt = A[pt]
    else:
        break

ans = 0
for i in range(n+1):
    if F[i]:
        ans += 1
print(ans)
