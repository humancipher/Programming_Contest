N,M,C = map(int,input().split())
B = list(map(int,input().split()))
A = [list(map(int,input().split())) for _ in range(N)]

count = 0
for i in range(N):
    s = C
    for j in range(M):
        s += A[i][j]*B[j]
    if s > 0:
        count += 1

print(count)
