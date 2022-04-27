N,K = map(int,input().split())
d = []
A = []
for i in range(K):
    d.append(int(input()))
    A.append(list(map(int,input().split())))

S = [1 for _ in range(N)]
for i in range(K):
    for j in range(len(A[i])):
        S[A[i][j]-1] = 0

print(sum(S))
