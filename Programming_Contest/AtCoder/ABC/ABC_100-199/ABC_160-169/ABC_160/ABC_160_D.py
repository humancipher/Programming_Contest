N,X,Y = map(int,input().split())

D = [0 for _ in range(N+1)]
#D[i]:距離がiである頂点(a,b)(a!=b)の組の個数

def dist(i,j):
    return min(j-i,abs(X-i)+abs(j-Y)+1)

for i in range(1,N):
    for j in range(i+1,N+1):
        D[dist(i,j)] += 1

for k in range(1,N):
    print(D[k])
