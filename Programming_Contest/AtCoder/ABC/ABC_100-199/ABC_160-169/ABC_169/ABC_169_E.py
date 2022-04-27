def median(A,N):
    A.sort()
    if N % 2 == 1:
        return A[N//2]
    else:
        return A[(N-1)//2] + A[(N-1)//2+1]

def main():
    N = int(input())
    AB = [list(map(int,input().split())) for _ in range(N)]

    A = [AB[i][0] for i in range(N)]
    B = [AB[i][1] for i in range(N)]

    ans = median(B,N) - median(A,N) + 1
    print(ans)

if __name__ == "__main__":
    main()
