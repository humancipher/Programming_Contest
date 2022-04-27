from heapq import heapify,heappush,heappop
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
INF = 10**10

def dfs(G,D,X,now,par):
    HQ = list()
    heapify(HQ)
    heappush(HQ,-X[now])
    for nxt in G[now]:
        if nxt != par:
            HQC = dfs(G,D,X,nxt,now)
            while len(HQC) > 0:
                x = heappop(HQC)
                if x != -INF:
                    heappush(HQ,x)
                else:
                    break
    RHQ = list()
    cnt = 0
    while len(RHQ) < 20 and len(HQ) > 0:
        x = heappop(HQ)
        heappush(RHQ,-abs(x))
        D[now][cnt] = -abs(x)
        cnt += 1
    return RHQ
        
def main():
    n,q = map(int,input().split())
    X = list(map(int,input().split()))
    G = [list() for _ in range(n)]
    for _ in range(n-1):
        a,b = map(int,input().split())
        G[a-1].append(b-1)
        G[b-1].append(a-1)
    D = [[-INF] * 20 for _ in range(n)] #D[i][j]:i番目の頂点の部分木でj番目に大きいやつ
    dfs(G,D,X,0,-1)
    Ans = list()
    for _ in range(q):
        v,k = map(int,input().split())
        Ans.append(-D[v-1][k-1])
    for i in range(len(Ans)):
        print(Ans[i])

if __name__ == "__main__":
    main()
