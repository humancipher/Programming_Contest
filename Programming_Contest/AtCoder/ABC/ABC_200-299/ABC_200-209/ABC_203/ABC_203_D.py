import sys
input = sys.stdin.readline
from itertools import accumulate
INF = 10**10

def judge(A,n,k,x): #中央値が全部x以上か
    B = [[0] * (n+1) for _ in range(n+1)]
    for i in range(n):
        for j in range(n):
            if A[i][j] >= x:
                B[i+1][j+1] = 1
    for i in range(n+1):
        B[i] = list(accumulate(B[i]))
    for i in range(n):
        for j in range(n+1):
            B[i+1][j] += B[i][j]
    for i in range(k,n+1):
        for j in range(k,n+1):
            tmp = B[i][j] - B[i-k][j] - B[i][j-k] + B[i-k][j-k]
            if tmp < k**2//2 + 1:
                return False
    return True

def main():
    n,k = map(int,input().split())
    A = [list(map(int,input().split())) for _ in range(n)]
    left,right = -1,INF
    while right - left > 1:
        mid = (left+right)//2
        if judge(A,n,k,mid):
            left = mid
        else:
            right = mid
    print(left)

if __name__ == "__main__":
    main()
