import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline
mod = 998244353

def dfs(G,Cnt,Map,now,par,go):
    if now == go:
        return True
    for nxt in G[now]:
        if nxt != par:
            if dfs(G,Cnt,Map,nxt,now,go):
                a = min(now,nxt)
                b = max(now,nxt)
                Cnt[Map[(a,b)]] += 1
                return True
    return False

def main():
    n,m,k = map(int,input().split())
    A = list(map(int,input().split()))
    G = [list() for _ in range(n)]
    Cnt = []
    Map = dict()
    for _ in range(n-1):
        u,v  = map(int,input().split())
        u,v = u-1,v-1
        G[u].append(v)
        G[v].append(u)
        a = min(u,v)
        b = max(u,v)
        if (a,b) not in Map:
            Map[(a,b)] = len(Map)
            Cnt.append(0)
    for i in range(m-1):
        a,b = A[i]-1,A[i+1]-1
        dfs(G,Cnt,Map,a,-1,b)
    sc = sum(Cnt)
    dp = [0] * (sc+1) #dp[j]:i番目までの辺で持って来て和をjにするパターン数
    dp[0] = 1

    if (sc+k) % 2 == 0 and sc+k >= 0 and k <= sc:
        for i in range(len(Cnt)):
            ndp = [0] * (sc+1)
            for j in range(sc+1):
                ndp[j] += dp[j]
                ndp[j] %= mod
                if j+Cnt[i] <= sc:
                    ndp[j+Cnt[i]] += dp[j]
                    ndp[j+Cnt[i]] %= mod
            dp = ndp
        print(dp[(sc+k)//2])
    else:
        print(0)

if __name__ == "__main__":
    main()
