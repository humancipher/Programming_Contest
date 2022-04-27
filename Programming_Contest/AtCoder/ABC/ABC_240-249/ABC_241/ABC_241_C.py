n = int(input())
S = [list(input()) for _ in range(n)]
ans = False
#横
D = [[0] * (n+1) for _ in range(n+1)]
for i in range(n):
    for j in range(n):
        if S[i][j] == "#":
            D[i+1][j+1] = 1
for i in range(n+1):
    for j in range(n):
        D[i][j+1] += D[i][j]
for i in range(n+1):
    for j in range(n-5):
        if D[i][j+6] - D[i][j] >= 4:
            ans = True

#縦
D = [[0] * (n+1) for _ in range(n+1)]
for i in range(n):
    for j in range(n):
        if S[i][j] == "#":
            D[i+1][j+1] = 1
for j in range(n+1):
    for i in range(n):
        D[i+1][j] += D[i][j]
for i in range(n-5):
    for j in range(n+1):
        if D[i+6][j] - D[i][j] >= 4:
            ans = True

#斜め1
D = [[0] * (n+1) for _ in range(n+1)]
for i in range(n):
    for j in range(n):
        if S[i][j] == "#":
            D[i+1][j+1] = 1
for j in range(n):
    for i in range(n):
        D[i+1][j+1] += D[i][j]
for i in range(n-5):
    for j in range(n-5):
        if D[i+6][j+6] - D[i][j] >= 4:
            ans = True

#斜め2
D = [[0] * (n+1) for _ in range(n+1)]
for i in range(n):
    for j in range(n):
        if S[i][j] == "#":
            D[i+1][n-j] = 1
for j in range(n):
    for i in range(n):
        D[i+1][j+1] += D[i][j]
for i in range(n-5):
    for j in range(n-5):
        if D[i+6][j+6] - D[i][j] >= 4:
            ans = True

if ans:
    print("Yes")
else:
    print("No")