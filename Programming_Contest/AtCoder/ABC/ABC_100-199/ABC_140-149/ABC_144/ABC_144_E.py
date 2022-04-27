def judge(A,F,n,k,key):
    #スコアをkey以下にできるかどうか
    #A:降順
    #F:昇順
    cnt = 0 #修行回数
    for i in range(n):
        mokuhyo = key // F[i]
        diff = max(0,A[i]-mokuhyo)
        cnt += diff
    return cnt <= k

def main():
    n,k = map(int,input().split())
    A = list(map(int,input().split()))
    F = list(map(int,input().split()))
    A.sort(reverse=True)
    F.sort()
    left,right = -1,10**13
    while right - left > 1:
        mid = (left+right)//2
        if judge(A,F,n,k,mid):
            right = mid
        else:
            left = mid
    print(right)

if __name__ == "__main__":
    main()
