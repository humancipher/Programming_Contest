N = int(input())
X = list(map(int,input().split()))

INF = 10**7

def cost(x,p):
    return (x-p)**2

X.sort()
ans = INF
for p in range(X[0],X[N-1]+1):
    sum = 0
    for i in range(N):
        sum += cost(X[i],p)
    ans = min(ans,sum)

print(ans)
