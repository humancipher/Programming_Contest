from sys import stdin
input = stdin.readline

n,q = map(int,input().split())
A = list(map(int,input().split()))
Ans = []
pt = 0
for _ in range(q):
    t,x,y = map(int,input().split())
    if t == 1:
        A[(pt+x-1)%n],A[(pt+y-1)%n] = A[(pt+y-1)%n],A[(pt+x-1)%n]
    if t == 2:
        pt -= 1
        pt %= n
    if t == 3:
        Ans.append(A[(pt+x-1)%n])
for i in range(len(Ans)):
    print(Ans[i])