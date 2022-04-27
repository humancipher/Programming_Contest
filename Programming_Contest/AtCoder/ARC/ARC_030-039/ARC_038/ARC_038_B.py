V = [(0,1),(1,0),(1,1)]

h,w = map(int,input().split())
S = [input() for _ in range(h)]

dp = [[0] * w for _ in range(h)]
#dp[i][j]:(i,j)からスタートした場合の勝敗(dp[i][j]==0なら後手勝ち)

for i in reversed(range(h)):
    for j in reversed(range(w)):
        result = 0 #勝ちパターン(負けパターンへの遷移)ありかどうか
        for vx,vy in V:
            if i+vx < h and j+vy < w:
                if S[i+vx][j+vy] == "." and dp[i+vx][j+vy] == 0:
                    result = 1
        dp[i][j] = result

if dp[0][0] == 0:
    print("Second")
else:
    print("First")
