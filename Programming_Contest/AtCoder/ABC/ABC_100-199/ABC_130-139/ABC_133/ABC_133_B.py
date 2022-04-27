N,D = map(int,input().split())
X = [list(map(int,input().split())) for _ in range(N)]

def dist_sq(x,y):
    ret = 0
    for i in range(D):
        ret += (x[i]-y[i])**2
    return ret

SQ,a = set([]),1
while a**2 <= 40**2*D:
    SQ.add(a**2)
    a += 1

ans = 0
for i in range(N):
    for j in range(i+1,N):
        if dist_sq(X[i],X[j]) in SQ:
            ans += 1

print(ans)
