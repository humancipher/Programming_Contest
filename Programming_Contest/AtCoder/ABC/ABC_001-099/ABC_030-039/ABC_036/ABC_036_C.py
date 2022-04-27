from bisect import bisect_left

def solve(A,N):
    B = list(set(A))
    B.sort()

    C = [None for _ in range(N)]

    for i in range(N):
        C[i] = bisect_left(B,A[i])

    return C

def main():
    N = int(input())
    A = [int(input()) for _ in range(N)]

    ans = solve(A,N)

    for i in range(N):
        print(ans[i])

if __name__ == "__main__":
    main()
