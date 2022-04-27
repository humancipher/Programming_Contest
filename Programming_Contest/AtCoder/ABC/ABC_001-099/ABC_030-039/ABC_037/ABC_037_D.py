mod = 10**9+7

def rec_cal(A,DP,H,W,x,y): #座標(x,y)をスタートとする経路数
    ans = 0
    V = [(0,1),(0,-1),(1,0),(-1,0)]
    for dx,dy in V:
        if 0 <= x+dx < H and 0 <= y+dy < W:
            if A[x][y] > A[x+dx][y+dy]:
                if DP[x+dx][y+dy] == None:
                    ans += rec_cal(A,DP,H,W,x+dx,y+dy)
                else:
                    ans += DP[x+dx][y+dy]
                ans %= mod
    ans += 1
    ans %= mod
    DP[x][y] = ans
    return ans

def solve(A,H,W):
    DP = [[None] * (W) for _ in range(H)] #DP[i][j]:(i,j)をスタートとする経路数
    ans = 0
    for i in range(H):
        for j in range(W):
            ans += rec_cal(A,DP,H,W,i,j)
            ans %= mod
    return ans

def main():
    H,W = map(int,input().split())
    A = [list(map(int,input().split())) for _ in range(H)]
    print(solve(A,H,W))

if __name__ == "__main__":
    main()
