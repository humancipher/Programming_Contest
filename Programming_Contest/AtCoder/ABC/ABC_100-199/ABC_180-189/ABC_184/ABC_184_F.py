from bisect import bisect_left

INF = 1 << 60

def half(A):
    n = len(A)
    Ans = list()
    Ans_set = set()
    for i in range(2**n):
        tmp = 0
        for b in range(n):
            if i & 2**b:
                tmp += A[b]
        if tmp not in Ans_set:
            Ans_set.add(tmp)
            Ans.append(tmp)
    Ans.sort()
    return Ans

def solve(A,N,T):
    if N >= 2:
        A.sort()
        L = half(A[:N//2])
        R = half(A[N//2:])
        R.append(INF)
        ans = 0
        for i in range(len(L)):
            if L[i] > T:
                break
            j = bisect_left(R,T - L[i])
            if R[j] != T - L[i] and j > 0:
                j -= 1
            if L[i] + R[j] <= T:
                ans = max(ans,L[i] + R[j])
        return ans
    else:
        if A[0] <= T:
            return A[0]
        else:
            return 0

def main():
    N,T = map(int,input().split())
    A = list(map(int,input().split()))
    print(solve(A,N,T))

if __name__ == "__main__":
    main()
