INF = 10**15

def solve(XC,N):
    CL = [None for _ in range(N+1)] #最左
    CR = [None for _ in range(N+1)] #最右
    for x,c in XC:
        if CL[c] == None:
            CL[c],CR[c] = x,x
        else:
            CL[c] = min(CL[c],x)
            CR[c] = max(CR[c],x)
    dp = [[INF,INF] for i in range(N+1)] #dp[i][0]:色iを踏んで最左に来るまでのコスト
    dp[0] = [0,0]
    cl,cr = 0,0 #1個前の色の最左、最右
    for i in range(1,N+1):
        if CL[i] == None: #ボールなし
            dp[i][0] = dp[i-1][0]
            dp[i][1] = dp[i-1][1]
        else: #ボールあり
            #左->左
            if cl <= CR[i]:
                dp[i][0] = min(dp[i][0],dp[i-1][0]+2*CR[i]-CL[i]-cl)
            else:
                dp[i][0] = min(dp[i][0],dp[i-1][0]+cl-CL[i])
            #左->右
            if cl >= CL[i]:
                dp[i][1] = min(dp[i][1],dp[i-1][0]+CR[i]-2*CL[i]+cl)
            else:
                dp[i][1] = min(dp[i][1],dp[i-1][0]+CR[i]-cl) #添え字には気を付けよう
            #右->左
            if cr <= CR[i]:
                dp[i][0] = min(dp[i][0],dp[i-1][1]+2*CR[i]-CL[i]-cr)
            else:
                dp[i][0] = min(dp[i][0],dp[i-1][1]+cr-CL[i])
            #右->右
            if cr >= CL[i]:
                dp[i][1] = min(dp[i][1],dp[i-1][1]+CR[i]-2*CL[i]+cr)
            else:
                dp[i][1] = min(dp[i][1],dp[i-1][1]+CR[i]-cr)
            cl,cr = CL[i],CR[i]
    return min(dp[N][0]+abs(cl),dp[N][1]+abs(cr))

def main():
    N = int(input())
    XC = [list(map(int,input().split())) for _ in range(N)]
    print(solve(XC,N))

if __name__ == "__main__":
    main()
            
            