N,M = map(int,input().split())
A = list(map(int,input().split()))

ans,S = 0,sum(A)
for i in range(N):
    if A[i] >= S/(4*M):
        ans += 1

if ans >= M:
    print("Yes")
else:
    print("No")
