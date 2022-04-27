INF = 10**18

def rec(dp,B,n,i,j):
    if dp[i][j] != None:
        return dp[i][j]
    else:
        ans = INF
        for k in range(i,j):
            ans = min(ans,rec(dp,B,n,i,k)+rec(dp,B,n,k+1,j)+B[j+1]-B[i])
        dp[i][j] = ans
        return ans

def main():
    n = int(input())
    A = list(map(int,input().split()))

    B = [0] + [A[i] for i in range(n)]
    for i in range(1,n+1):
        B[i] += B[i-1]
    dp = [[None for _ in range(n)] for _ in range(n)]
    #dp[i][j]:区間[i,j]での最適解

    for i in range(n):
        dp[i][i] = 0

    print(rec(dp,B,n,0,n-1))

if __name__ == "__main__":
    main()
