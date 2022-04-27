from sys import setrecursionlimit
setrecursionlimit(10**6)

def dfs(G,dp,now,par):
    if dp[now] == None:
        dp[now] = 0
    for nxt,dist in G[now]:
        if nxt != par:
            if dp[nxt] == None:
                dp[nxt] = dp[now] + dist
                dfs(G,dp,nxt,now)

def main():
    import sys
    input = sys.stdin.readline
    n,m = map(int,input().split())
    G = [list() for _ in range(n)]
    Inp = []
    for _ in range(m):
        l,r,d = map(int,input().split())
        G[l-1].append((r-1,d))
        G[r-1].append((l-1,-d))
        Inp.append((l-1,r-1,d))
    dp = [None] * n
    for i in range(n):
        if dp[i] == None:
            dfs(G,dp,i,-1)
    ans = True
    for a,b,c in Inp:
        if dp[b] != dp[a] + c:
            ans = False
            break
    if ans:
        print("Yes")
    else:
        print("No")

if __name__ == "__main__":
    main()
