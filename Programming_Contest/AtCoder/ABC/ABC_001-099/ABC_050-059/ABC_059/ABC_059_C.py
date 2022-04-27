def main():
    import sys
    input = sys.stdin.readline
    n = int(input())
    A = list(map(int,input().split()))
    B = [A[i] for i in range(n)]
    # 負　正　負　...
    if A[0] >= 0:
        cnt = A[0]+1
        tmp = -1
    else:
        cnt = 0
        tmp = A[0]
    for i in range(1,n):
        if i % 2 == 0:
            if tmp + A[i] >= 0:
                cnt += tmp+A[i]+1 #tmp+A[i]-cnt == -1
                tmp = -1
            else:
                tmp += A[i]
        else:
            if tmp + A[i] <= 0:
                cnt += 1-tmp-A[i] #tmp+A[i]+cnt == 1
                tmp = 1
            else:
                tmp += A[i]
    ans = cnt
    # 正　負　正...
    if A[0] <= 0:
        cnt = 1-A[0]
        tmp = 1
    else:
        cnt = 0
        tmp = A[0]
    for i in range(1,n):
        if i % 2 != 0:
            if tmp + A[i] >= 0:
                cnt += tmp+A[i]+1 #tmp+A[i]-cnt == -1
                tmp = -1
            else:
                tmp += A[i]
        else:
            if tmp + A[i] <= 0:
                cnt += 1-tmp-A[i] #tmp+A[i]+cnt == 1
                tmp = 1
            else:
                tmp += A[i]
    ans = min(ans,cnt)
    print(ans)

if __name__ == "__main__":
    main()
