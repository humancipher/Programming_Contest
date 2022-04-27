def main():
    N = int(input())
    A = list(map(int,input().split()))

    A.sort()

    B = [A[i] for i in range(N)]
    for i in range(1,N):
        B[i] += B[i-1]

    ans = 1
    for i in reversed(range(N-1)):
        if 2*B[i] >= A[i+1]:
            ans += 1
        else:
            break

    print(ans)

if __name__ == "__main__":
    main()
