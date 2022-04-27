from sys import setrecursionlimit

setrecursionlimit(10**5) #再帰を使うときは気を付けよう

def dfs(G,T,Use,now):
    if Use[now]:
        for nxt in G[now]:
            dfs(G,T,Use,nxt)
        T.append(now)
        Use[now] = False

def TPS(G,n):
    T = []
    Use = [True for _ in range(n+1)]
    for i in range(1,n+1):
        dfs(G,T,Use,i)
    for i in range(n//2):
        T[i],T[-1-i] = T[-1-i],T[i]
    return T

def solve(G,n):
    tps = TPS(G,n)
    dp = [0 for _ in range(n+1)] #dp[i]:頂点iからの最長パスの長さ
    for i in range(n):
        for nxt in G[tps[i]]:
            dp[nxt] = max(dp[nxt],dp[tps[i]]+1)
    return max(dp)

def main():
    n,m = map(int,input().split())
    G = [set() for _ in range(n+1)]
    for _ in range(m):
        x,y = map(int,input().split())
        G[x].add(y)
    print(solve(G,n))

if __name__ == "__main__":
    main()
