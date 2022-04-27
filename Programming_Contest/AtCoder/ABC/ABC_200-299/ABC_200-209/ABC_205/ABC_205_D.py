from bisect import bisect_right

def solve(A,A_set,k):
    left,right = 0,10**18 + 10**6 #left <= ans < right
    while right - left > 1:
        mid = (left + right) // 2
        mbr = mid - bisect_right(A,mid)
        if mid not in A_set:
            if mbr == k:
                return mid
            elif mbr < k:
                left = mid
            else:
                right = mid
        else:
            if mbr < k:
                left = mid
            else:
                right = mid
    return left

def main():
    n,q = map(int,input().split())
    A = list(map(int,input().split()))
    A_set = set(A)
    K = [int(input()) for _ in range(q)]
    for i in range(q):
        print(solve(A,A_set,K[i]))

if __name__ == "__main__":
    main()
