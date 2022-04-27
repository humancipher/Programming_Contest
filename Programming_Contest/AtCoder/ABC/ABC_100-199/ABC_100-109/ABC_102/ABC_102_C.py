from itertools import accumulate
from bisect import bisect_left

INF = 1 << 60

def solve(A,N):
    for i in range(N):
        A[i] -= (i+1)
    A.sort()
    if A[0] < 0:
        buf = A[0]
        for i in range(N):
            A[i] -= buf
    
    B = set()
    for a in A:
        B.add(a)
    A_rui = list(accumulate(A))
    ans = INF
    for b in B:
        i = bisect_left(A,b)
        if i > 0:
            ans = min(ans,A_rui[N-1] - 2*A_rui[i-1] + b*(2*i-N))
        else:
            ans = min(ans,A_rui[N-1]- b*N)
    return ans

def main():
    N = int(input())
    A = list(map(int,input().split()))

    print(solve(A,N))

if __name__ == "__main__":
    main()
