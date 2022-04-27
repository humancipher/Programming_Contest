from bisect import bisect_left,bisect_right
from sys import stdin
input = stdin.readline
INF = 10**6

def main():
    n = int(input())
    A = list(map(int,input().split()))
    B = [A[n-i-1] for i in range(n)]
    L = [INF] * (n+1)
    R = [INF] * (n+1)
    P = [0] * (n+1)
    Q = [0] * (n+1)
    for i in range(n):
        ptl = bisect_left(L,A[i])
        L[ptl] = A[i]
        P[i] = ptl + 1
    for i in range(n):
        ptr = bisect_left(R,B[i])
        R[ptr] = B[i]
        Q[i] = ptr + 1
    ans = 0
    for i in range(n):
        ans = max(ans,P[i]+Q[i]-1)
    print(ans)

if __name__ == "__main__":
    main()
