n = int(input())
S = list(map(int,input().split()))

Pat = set()
for a in range(1,400):
    for b in range(1,400):
        Pat.add(4*a*b+3*a+3*b)

ans = 0
for i in range(n):
    if S[i] not in Pat:
        ans += 1
print(ans)
