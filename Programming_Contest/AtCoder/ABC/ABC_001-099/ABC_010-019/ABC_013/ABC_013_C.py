INF = 10**12

def mokuteki(a,c,x,y):
    return a*x + c*y

n,h = map(int,input().split())
a,b,c,d,e = map(int,input().split())

#x=0,1,...,nの場合でのyを調べてその最適解を選ぶ
ans = INF
for x in range(n+1):
    y = (e*(n-x)-b*x-h+1)//(d+e)
    if (e*(n-x)-b*x-h+1) % (d+e) != 0:
        y += 1
    ans = min(ans,mokuteki(a,c,x,max(0,y)))
print(ans)