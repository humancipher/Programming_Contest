from operator import le


def judge_ave(A,n,x):#平均x以上にできるかどうか
    dp = [[0] * 2 for _ in range(n+1)]
    #dp[i+1][0]:A[i]までを見ての平均の最大値（A[i]未選択)
    for i in range(n):
        dp[i+1][0] = dp[i][1]
        dp[i+1][1] = max(dp[i][0],dp[i][1])+(A[i]-x)
    return max(dp[n][0],dp[n][1]) >= 0

def judge_med(A,n,x):#中央値x以上にできるかどうか
    dp = [[0] * 2 for _ in range(n+1)]
    #dp[i+1][0]:A[i]までを見て(x以上の個数)-(x未満の個数)(A[i]未選択)
    for i in range(n):
        dp[i+1][0] = dp[i][1]
        dp[i+1][1] = max(dp[i][0],dp[i][1])
        if A[i] >= x:
            dp[i+1][1] += 1
        else:
            dp[i+1][1] -= 1
    return max(dp[n][0],dp[n][1]) > 0

def solve(A,n):
    Ans = []
    left,right = -1,10**9+1
    while (right-left) > 10**(-4):
        mid = (left+right)/2
        if judge_ave(A,n,mid):
            left = mid
        else:
            right = mid
    Ans.append(left)
    left,right = -1,10**9+1
    while (right-left) > 1:
        mid = (left+right)//2
        if judge_med(A,n,mid):
            left = mid
        else:
            right = mid
    Ans.append(left)
    return Ans

def main():
    n = int(input())
    A = list(map(int,input().split()))
    Ans = solve(A,n)
    print(Ans[0])
    print(Ans[1])

if __name__ == "__main__":
    main()
