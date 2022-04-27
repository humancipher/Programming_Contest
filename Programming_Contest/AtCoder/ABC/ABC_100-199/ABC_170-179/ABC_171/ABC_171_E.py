def solve(A,N):
    xor_sum = 0
    for i in range(N):
        xor_sum ^= A[i]

    B = [xor_sum ^ A[i] for i in range(N)]

    return B

def main():
    N = int(input())
    A = list(map(int,input().split()))

    ans = solve(A,N)

    print(" ".join(map(str,ans)))

if __name__ == "__main__":
    main()
