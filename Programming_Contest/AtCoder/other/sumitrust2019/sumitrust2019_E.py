def col_count(A,N,M):
    col = [[0,0,0] for _ in range(N+1)]
    for i in range(N):
        for j in range(3):
            col[i+1][j] = col[i][j]
        for j in range(3):
            if col[i][j] == A[i]:
                col[i+1][j] += 1
                break

    output = 1
    for i in range(N):
        cnt = 0
        for j in range(3):
            if col[i][j] == A[i]:
                cnt += 1

        output *= cnt
        output %= M
    return output

def main():
    N = int(input())
    A = list(map(int,input().split()))
    M = 10**9+7

    print(col_count(A,N,M))

if __name__ == "__main__":
    main()
