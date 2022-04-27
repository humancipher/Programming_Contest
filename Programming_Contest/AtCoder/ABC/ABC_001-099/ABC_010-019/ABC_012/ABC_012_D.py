INF = 10**10

def warshallfloyd(GD,n):
    D = [[INF] * n for _ in range(n)]
    for i in range(n):
        D[i][i] = 0
    for i in range(n):
        for j in range(n):
            if (i,j) in GD:
                D[i][j] = GD[(i,j)]
    for k in range(n):
        for i in range(n):
            for j in range(n):
                D[i][j] = min(D[i][j],D[i][k]+D[k][j])
    ans = INF
    for i in range(n):
        ans = min(ans,max(D[i]))
    return ans

n,m = map(int,input().split())
G = [set() for _ in range(n+1)]
GD = dict()
for _ in range(m):
    a,b,t = map(int,input().split())
    GD[(a-1,b-1)] = t
    GD[(b-1,a-1)] = t

ans = warshallfloyd(GD,n)
print(ans)