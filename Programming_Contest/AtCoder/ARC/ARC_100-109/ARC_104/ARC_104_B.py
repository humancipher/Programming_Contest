N,S = input().split()

N = int(N)

A = [0 for _ in range(N+1)]
T = [0 for _ in range(N+1)]
C = [0 for _ in range(N+1)]
G = [0 for _ in range(N+1)]

for i in range(N):
    if S[i] == "A":
        A[i+1] = 1
    if S[i] == "T":
        T[i+1] = 1
    if S[i] == "C":
        C[i+1] = 1
    if S[i] == "G":
        G[i+1] = 1

for i in range(1,N):
    A[i+1] += A[i]
    T[i+1] += T[i]
    C[i+1] += C[i]
    G[i+1] += G[i]

ans = 0
for i in range(N+1):
    for j in range(i+1,N+1):
        if ( (A[j] - A[i]) == (T[j] - T[i]) and (G[j] - G[i]) == (C[j] - C[i])):
            ans += 1

print(ans)
