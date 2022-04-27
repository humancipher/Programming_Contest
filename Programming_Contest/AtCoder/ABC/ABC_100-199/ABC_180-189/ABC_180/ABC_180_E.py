INF = 2 << 60

def dist(a,b):
    return abs(a[0]-b[0]) + abs(a[1]-b[1]) + max(0,b[2]-a[2])

def calHW(n):
    b = bin(n)
    return b.count("1")

def solve(XYZ,N):
    HW = [set() for _ in range(N+1)] #HW[i]:ハミング重みがiになる数の集合
    for i in range(2**N):
        HW[calHW(i)].add(i)
    dp = [[INF for _ in range(2**N)] for _ in range(N)] #dp[i][S]: 最後に街iに来て訪れた町がSであるときの最短距離
    for i in range(N):
        dp[i][2**i] = dist(XYZ[0],XYZ[i]) #HW[1]を初期化
    
    for hw in range(2,N+1):
        for s in HW[hw]:
            for i in range(N):
                if (s ^ 2**i) in HW[hw-1]:
                    for j in range(N):
                        if (s ^ 2**i) & 2**j != 0:
                            dp[i][s] = min(dp[i][s],dp[j][s ^ 2**i] + dist(XYZ[j],XYZ[i]))
    
    return dp[0][2**N-1]

def main():
    N = int(input())
    XYZ = [tuple(map(int,input().split())) for _ in range(N)]

    ans = solve(XYZ,N)
    print(ans)

if __name__ == "__main__":
    main()
