def check(x): #xが阿弥陀の横パターンとして成立するかどうか
    flag = False
    while x > 0:
        if x % 2 != 0:
            if flag:
                return False
            else:
                flag = True
        else:
            flag = False
        x //= 2
    return True

def main():
    import sys
    input = sys.stdin.readline
    mod = 10**9+7
    H,W,K = map(int,input().split())
    dp = [[0] * W for _ in range(H+1)]
    dp[0][0] = 1
    #dp[i][j]:高さiの時点でj列目にいるパターン数
    P = set()
    for i in range(2**(W-1)):
        if check(i):
            P.add(i)
    for i in range(H):
        for p in P:
            F = [k for k in range(W)] #F[k]:kの遷移先
            for k in range(W-1):
                if 2**k & p:
                    F[k],F[k+1] = F[k+1],F[k]
            for k in range(W):
                dp[i+1][F[k]] += dp[i][k]
                dp[i+1][F[k]] %= mod
    print(dp[H][K-1])

if __name__ == "__main__":
    main()
