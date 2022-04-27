from itertools import accumulate

N = int(input())
A = list(map(int,input().split()))

B = list(accumulate(A))
C = list(accumulate(B))

ans = 0
maxB = [0 for _ in range(N)]

for i in range(N):
    if i >= 1:
        maxB[i] = max(maxB[i-1],B[i])
    else:
        maxB[i] = B[0]

for i in range(N):
    ans = max(ans,C[i])
    if i >= 1:
        ans = max(ans,C[i-1] + max(0,maxB[i-1]))

print(ans)
