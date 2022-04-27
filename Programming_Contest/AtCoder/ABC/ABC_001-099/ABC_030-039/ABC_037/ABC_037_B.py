N,Q = map(int,input().split())
LRT = [list(map(int,input().split())) for _ in range(Q)]

A = [0 for _ in range(N+1)]

for i in range(Q):
    for j in range(LRT[i][0],LRT[i][1]+1):
        A[j] = LRT[i][2]

for i in range(1,N+1):
    print(A[i])
