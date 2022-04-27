def solve(D,N):
    for i in range(N):
        D[i] = [0] + D[i]
    D = [[0]*(N+1)] + D
    for i in range(N+1):
        for j in range(N):
            D[i][j+1] += D[i][j]
    for i in range(N):
        for j in range(N+1):
            D[i+1][j] += D[i][j]
    
    Ans = [0 for _ in range(N**2+1)]
    for x in range(1,N+1):
        for y in range(1,N+1):
            for dx in range(x):
                for dy in range(y):
                    Ans[(x-dx)*(y-dy)] = +\
                    max(Ans[(x-dx)*(y-dy)],
                        D[x][y]-D[x][dy]-D[dx][y]+D[dx][dy])
    for i in range(N**2):
        Ans[i+1] = max(Ans[i+1],Ans[i])
    
    return Ans

def main():
    N = int(input())
    D = [list(map(int,input().split())) for _ in range(N)]
    Q = int(input())
    P = [int(input()) for _ in range(Q)]

    Ans = solve(D,N)
    for i in range(Q):
        print(Ans[P[i]])

if __name__ == "__main__":
    main()
