N = int(input())
A = [int(input()) for _ in range(N)]

S = set([])

ans = 0
for i in range(N):
    if A[i] in S:
        ans += 1
    else:
        S.add(A[i])

print(ans)
