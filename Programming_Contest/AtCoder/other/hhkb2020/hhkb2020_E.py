from re import U

mod = 10**9+7

h,w = map(int,input().split())
S = [input() for _ in range(h)]
k = 0
for i in range(h):
    for j in range(w):
        if S[i][j] == ".":
            k += 1
X = [[0] * w for _ in range(h)] #横の連続数
Y = [[0] * w for _ in range(h)] #縦の連続数
for i in range(h):
    for j in range(w):
        if S[i][j] == ".":
            X[i][j] = 1
            Y[i][j] = 1
for i in range(h):
    for j in range(1,w):
        if X[i][j] != 0:
            X[i][j] += X[i][j-1]
for j in range(w):
    for i in range(1,h):
        if Y[i][j] != 0:
            Y[i][j] += Y[i-1][j]
for i in range(h):
    for j in reversed(range(w-1)):
        if X[i][j] != 0:
            X[i][j] = max(X[i][j],X[i][j+1])
for j in range(w):
    for i in reversed(range(h-1)):
        if Y[i][j] != 0:
            Y[i][j] = max(Y[i][j],Y[i+1][j])

ans = 0
p2k = pow(2,k,mod)
D = dict() #計算済のpowを覚えておきたい
for i in range(h):
    for j in range(w):
        if S[i][j] == ".":
            diff = p2k
            if (k-X[i][j]-Y[i][j]+1) not in D:
                tmp = pow(2,k-X[i][j]-Y[i][j]+1,mod)
                D[(k-X[i][j]-Y[i][j]+1)] = tmp
                diff -= tmp
            else:
                diff -= D[(k-X[i][j]-Y[i][j]+1)]
            ans += diff
            ans %= mod
print(ans)