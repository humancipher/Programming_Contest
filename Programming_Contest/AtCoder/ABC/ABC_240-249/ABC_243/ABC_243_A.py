v,a,b,c, = map(int,input().split())
X = [a,b,c]
v %= (a+b+c)
Ans = ["F","M","T"]
for i in range(3):
    if v < X[i]:
        print(Ans[i])
        break
    else:
        v -= X[i]