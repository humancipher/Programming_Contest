#main関数修正中
#ちょうどk個のパターンなしの場合が怪しい？

INF = 10**10

def judge(A,n,p,x):
    B = [[None] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if A[i][j] == -1:
                B[i][j] = x
            else:
                B[i][j] = A[i][j]
    for h in range(n):
        for i in range(n):
            for j in range(n):
                B[i][j] = min(B[i][j],B[i][h]+B[h][j])
    cnt = 0
    for i in range(n):
        for j in range(i+1,n):
            if B[i][j] <= p:
                cnt += 1
    return cnt

def main():
    n,p,k = map(int,input().split())
    A = [list(map(int,input().split())) for _ in range(n)]
    if judge(A,n,p,INF) > k or judge(A,n,p,1) < k:
        ans = 0
    elif judge(A,n,p,INF) == k:
        ans = INF
    else:
        left,right = 1,INF #judge(left) >= k judge(right) < k
        #k個以上になるxの最大値
        while right - left > 1:
            mid = (left+right)//2
            if judge(A,n,p,mid) >= k:
                left = mid
            else:
                right = mid
        upper = left
        left,right = 1,INF
        #k+1個以上になるxの最大値
        while right - left > 1:
            mid = (left+right)//2
            if judge(A,n,p,mid) >= k+1:
                left = mid
            else:
                right = mid
        lower = left
        ans = (upper-lower)
    if ans == INF:
        print("Infinity")
    else:
        print(ans)

if __name__ == "__main__":
    main()
