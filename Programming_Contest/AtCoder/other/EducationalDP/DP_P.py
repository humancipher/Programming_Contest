from sys import setrecursionlimit
setrecursionlimit(10**6)
mod = 10**9+7

def dfs(dp,G,now,par):
    kuro,siro = 1,1 #頂点nowでの黒,白のパターン数
    for nxt in G[now]:
        if nxt != par:
            (b,w) = dfs(dp,G,nxt,now)
            siro *= (b+w) #白の直下はどっちでもよい
            siro %= mod
            kuro *= w #黒の直下は白しかダメ
            kuro %= mod
    dp[now] = [kuro,siro]
    return (kuro,siro)

def main():
    n = int(input())
    G = [list() for _ in range(n)]
    for _ in range(n-1):
        x,y = map(int,input().split())
        G[x-1].append(y-1)
        G[y-1].append(x-1)
    dp = [[0,0] for _ in range(n)]
    dfs(dp,G,0,-1)
    ans = (dp[0][0] + dp[0][1]) % mod
    print(ans)

if __name__ == "__main__":
    main()
