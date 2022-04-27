INF = 10**10
n = int(input())
ans = INF
lmax,rmin = -INF,INF
for i in range(n):
    l,r = map(int,input().split())
    lmax = max(lmax,l)
    rmin = min(rmin,r)
    x = (lmax+rmin)//2
    print(max(lmax-x,0,x-rmin))
