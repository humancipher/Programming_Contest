n,a,b = map(int,input().split())
p,q,r,s = map(int,input().split())

a -= 1
b -= 1
p -= 1
q -= 1
r -= 1
s -= 1
C = [[False] * (s-r+1) for _ in range(q-p+1)]

for i in range(q-p+1):
    for j in range(s-r+1):
        if abs(i+p-a) == abs(j+r-b):
            C[i][j] = True

Ans = [[] for _ in range(q-p+1)]
for i in range(q-p+1):
    for j in range(s-r+1):
        if C[i][j]:
            Ans[i].append("#")
        else:
            Ans[i].append(".")
    Ans[i] = "".join(Ans[i])

for i in range(q-p+1):
    print(Ans[i])