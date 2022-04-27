h,w,d = map(int,input().split())
A = [list(map(int,input().split())) for _ in range(h)]
D = dict()
for i in range(h):
    for j in range(w):
        D[A[i][j]] = (i,j)
q = int(input())
LR = [list(map(int,input().split())) for _ in range(q)]

Memo = [[0] * (h*w//d + 1) for _ in range(d)]
for i in range(d):
    for j in range(1,len(Memo[i])):
        if i+(j-1)*d in D and i+j*d in D:
            (x0,y0) = D[i+(j-1)*d]
            (x1,y1) = D[i+j*d]
            Memo[i][j] = Memo[i][j-1] + abs(x0-x1) + abs(y0-y1)

Ans = []
for i in range(q):
    l,r = LR[i][0],LR[i][1]
    sho,amari = (r-l) // d,l % d
    st = l // d
    Ans.append(Memo[amari][st+sho] - Memo[amari][st])

for i in range(len(Ans)):
    print(Ans[i])
