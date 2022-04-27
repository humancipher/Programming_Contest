N,Q = map(int,input().split())
LR = [list(map(int,input().split())) for _ in range(Q)]

A = [0 for _ in range(N)]

for i in range(Q):
    A[LR[i][0]-1] += 1
    if LR[i][1] < N:
        A[LR[i][1]] -= 1

for j in range(N-1):
    A[j+1] += A[j]

for j in range(N):
    A[j] %= 2

ans = ""
for j in range(N):
    ans += str(A[j])

print(ans)
