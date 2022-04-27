INF = 10**20

n,k = map(int,input().split())
X,Y = set(),set()
XY = list()
for _ in range(n):
    x,y = map(int,input().split())
    XY.append((x,y))
    X.add(x)
    Y.add(y)
X,Y = list(X),list(Y)
X.sort()
Y.sort()

ans = INF
for i in range(len(X)):
    for j in range(i+1,len(X)):
        xl,xr = X[i],X[j]
        pt1,pt2 = 0,0
        while pt1 < len(Y):
            while pt2 < len(Y):
                cnt = 0
                for x,y in XY:
                    if xl <= x <= xr and Y[pt1] <= y <= Y[pt2]:
                        cnt += 1
                if cnt < k:
                    pt2 += 1
                else:
                    break
            if pt2 < len(Y):
                ans = min(ans,(xr-xl) * (Y[pt2]-Y[pt1]))
            pt1 += 1
print(ans)