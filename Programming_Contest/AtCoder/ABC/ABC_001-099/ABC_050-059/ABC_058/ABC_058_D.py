mod = 10**9+7

n,m = map(int,input().split())
X = list(map(int,input().split()))
Y = list(map(int,input().split()))

DX = [X[i+1]-X[i] for i in range(n-1)]
DY = [Y[i+1]-Y[i] for i in range(m-1)]

sx,sy = 0,0
for i in range(n-1):
    left = i+1
    right = n-i-1
    sx += DX[i] * left * right
    sx %= mod
for i in range(m-1):
    left = i+1
    right = m-i-1
    sy += DY[i] * left * right
    sy %= mod
print(sx*sy % mod)