from time import sleep

n = int(input())
D = dict()
for _ in range(n):
    a,b = map(int,input().split())
    if a in D:
        D[a] += 1
    else:
        D[a] = 1
    if a+b in D:
        D[a+b] -= 1
    else:
        D[a+b] = -1
L = []
for d in D:
    if D[d] != 0:
        L.append([d,D[d]])
L.append([0,0])
L.append([10**10,0])
L.sort(key = lambda x:x[0])
K = [0] * (n+1)
cnt = 0
for i in range(len(L)-1):
    K[cnt] += L[i+1][0] - L[i][0]
    cnt += L[i+1][1]
print(" ".join(map(str,K[1:])))