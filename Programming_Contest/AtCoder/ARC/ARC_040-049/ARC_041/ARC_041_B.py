def solve(B,N,M):
    A = [[0 for _ in range(M+2)] for _ in range(N+2)]
    for i in range(N):
        B[i] = [0] + B[i] + [0]
    B = [[0] * (M+2)] + B + [[0] * (M+2)]

    Ans = []
    for i in range(1,N+1):
        for j in range(1,M+1):
            if i >= 2:
                A[i][j] = B[i-1][j] - (A[i-2][j] + A[i-1][j-1] + A[i-1][j+1])
            else:
                A[i][j] = B[i-1][j] - (A[i-1][j-1] + A[i-1][j+1])
        Ans.append("".join(map(str,A[i][1:M+1])))
    
    return Ans

def main():
    N,M = map(int,input().split())
    B = [list(input()) for _ in range(N)]
    for i in range(N):
        for j in range(M):
            B[i][j] = int(B[i][j])

    ans = solve(B,N,M)
    for i in range(N):
        print(ans[i])

if __name__ == "__main__":
    main()
