def judge(WP,k,x): #濃度x以上を達成可能かどうか
    A = []
    for w,p in WP:
        A.append(w*p-x*w)
    A.sort(reverse=True)
    return sum(A[:k]) >= 0

def solve(WP,k):
    left,right = 0,101
    while right - left > 10**(-10):
        mid = (left+right)/2
        if judge(WP,k,mid):
            left = mid
        else:
            right = mid
    return left

def main():
    n,k = map(int,input().split())
    WP = [list(map(int,input().split())) for _ in range(n)]
    print(solve(WP,k))

if __name__ == "__main__":
    main()
