def solve(A,N):
    A.sort(reverse = True)
    ans = A[0]
    if N % 2 == 0:
        pt = N // 2 - 1
        for i in range(1,pt+1):
            ans += (2 * A[i])
    else:
        pt = (N-1) // 2
        for i in range(1,pt):
            ans += (2 * A[i])
        ans += A[pt]
    return ans

def main():
    N = int(input())
    A = list(map(int,input().split()))

    print(solve(A,N))

if __name__ == "__main__":
    main()
