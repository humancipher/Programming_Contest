n = int(input())
TA = [list(map(int,input().split())) for _ in range(n)]

x,y = TA[0][0],TA[0][1]
for i in range(1,n):
    t,a = TA[i][0],TA[i][1]
    q = max((x+t-1)//t,(y+a-1)//a)
    x = t * q
    y = a * q
print(x+y)