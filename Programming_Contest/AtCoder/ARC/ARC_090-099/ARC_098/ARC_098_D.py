def solve(A,N):
    A = [0] + A
    B = [A[i] for i in range(N+1)]
    C = [A[i] for i in range(N+1)]
    for i in range(1,N+1):
        B[i] += B[i-1]
        C[i] ^= C[i-1]
    ans = 0
    for i in range(1,N+1):
        left,right = i,N+1
        while right - left > 1:
            mid = (left+right)//2
            if B[mid]-B[i-1] > C[mid]^C[i-1]:
                right = mid
            else:
                left = mid
        ans += (left-(i-1))
    return ans

def main():
    N = int(input())
    A = list(map(int,input().split()))
    print(solve(A,N))

if __name__ == "__main__":
    main()
