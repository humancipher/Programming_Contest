#修正中

h,w = map(int,input().split())
A = [input() for _ in range(h)]

dp = [[None] * w for _ in range(h)]
dp[h-1][w-1] = 0
#dp[i][j]:マス(i,j)からゲームを開始したときのTakahashiのスコア((i+j)%2==0のときTakahashiが先手)
#方針：ゴールから逆算する
for j in reversed(range(w-1)):
    if (A[h-1][j+1] == "+") != ((h+j) % 2 == 0):
        dp[h-1][j] = dp[h-1][j+1] + 1
    else:
        dp[h-1][j] = dp[h-1][j+1] - 1

for i in reversed(range(h-1)):
    if (A[i+1][w-1] == "+") != ((i+w) % 2 == 0):
        dp[i][w-1] = dp[i+1][w-1] + 1
    else:
        dp[i][w-1] = dp[i+1][w-1] - 1

for i in reversed(range(h-1)):
    for j in reversed(range(w-1)):
        pat1 = dp[i][j+1]
        if (A[i][j+1] == "+") != ((i+j+1) % 2 == 0):
            pat1 += 1
        else:
            pat1 -= 1
        pat2 = dp[i+1][j]
        if (A[i+1][j] == "+") != ((i+j+1) % 2 == 0):
            pat2 += 1
        else:
            pat2 -= 1
        if (i+j) % 2 == 0:
            dp[i][j] = max(pat1,pat2)
        else:
            dp[i][j] = min(pat1,pat2)
            
if dp[0][0] > 0:
    print("Takahashi")
elif dp[0][0] < 0:
    print("Aoki")
else:
    print("Draw")
