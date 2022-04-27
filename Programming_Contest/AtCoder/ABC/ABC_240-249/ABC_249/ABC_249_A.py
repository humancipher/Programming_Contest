a,b,c,d,e,f,x = map(int,input().split())
d1,d2 = 0,0
for i in range(x):
    if i % (a+c) < a:
        d1 += b
    if i % (d+f) < d:
        d2 += e
if d1 > d2:
    print("Takahashi")
if d1 < d2:
    print("Aoki")
if d1 == d2:
    print("Draw")