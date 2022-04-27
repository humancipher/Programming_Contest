n = 2**20
A = [-1] * n
Nxt = [i for i in range(n)]
q = int(input())
Ans = []
for i in range(q):
    t,x = map(int,input().split())
    if t == 1:
        y = x%n
        Tmp = [y]
        while A[y] != -1:
            y = Nxt[y]
            Tmp.append(y)
        A[y] = x
        for j in range(len(Tmp)):
            Nxt[Tmp[j]] = Nxt[(y+1)%n]
    else:
        print(A[x%n])