def solve(A,N):
    ans = 0
    for i in range(N-1):
        if A[i] == i+1:
            A[i],A[i+1] = A[i+1],A[i]
            ans += 1
    if A[N-1] == N:
        ans += 1
    return ans

def main():
    N = int(input())
    A = list(map(int,input().split()))
    print(solve(A,N))

if __name__ == "__main__":
    main()
