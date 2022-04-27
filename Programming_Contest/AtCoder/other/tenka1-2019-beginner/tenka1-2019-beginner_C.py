N = int(input())
S = list(input())

W = [0] * N
B = [0] * N

for i in range(N):
    if S[i] == "#":
        B[i] = 1
    else:
        W[i] = 1

for i in range(N-1):
    B[i+1] += B[i]

for i in reversed(range(N-1)):
    W[i] += W[i+1]

ans = N-1
for i in range(N):
    ans = min(ans,B[i] + W[i] - 1)

print(ans)
