from sys import setrecursionlimit
setrecursionlimit(10**6)

mod = 10**9+7

def dfs(G,dp,now,par,mod):
    siro,kuro = 1,1
    for nxt in G[now]:
        if nxt == par:
            continue
        (w,b) = dfs(G,dp,nxt,now,mod)
        siro *= (b+w) #白の下はどちらでもよい
        kuro *= w #黒の下は全部白以外ありえない
        siro %= mod
        kuro %= mod
    dp[now][0],dp[now][1] = siro,kuro
    return (siro,kuro)

def main():
    n = int(input())
    G = [list() for _ in range(n)]
    for _ in range(n-1):
        a,b = map(int,input().split())
        G[a-1].append(b-1)
        G[b-1].append(a-1)
    dp = [[0] * 2 for _ in range(n)]
    #dp[i][0]:i番目の頂点が白の場合のiを根とする部分木のパターン数
    #dp[i][1]:i番目の頂点が黒の場合のiを根とする部分木のパターン数
    dfs(G,dp,0,-1,mod)
    ans = (dp[0][0] + dp[0][1]) % mod
    print(ans)

if __name__ == "__main__":
    main()
