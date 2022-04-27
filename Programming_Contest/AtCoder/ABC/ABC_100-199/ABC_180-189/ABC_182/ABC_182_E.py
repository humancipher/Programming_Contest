def solve(B,L,H,W): #B[i][j]:マス(i,j)がブロックでないかどうか
    L2 = [[L[i][j] for j in range(W)] for i in range(H)]
    for i in range(H):
        for j in range(1,W):
            L[i][j] = (L[i][j-1] | L[i][j]) & B[i][j]
        for j in reversed(range(W-1)):
            L[i][j] = (L[i][j+1] | L[i][j]) & B[i][j]
    
    for j in range(W):
        for i in range(1,H):
            L2[i][j] = (L2[i-1][j] | L2[i][j]) & B[i][j]
        for i in reversed(range(H-1)):
            L2[i][j] = (L2[i+1][j] | L2[i][j]) & B[i][j]
    
    ans = 0
    for i in range(H):
        for j in range(W):
            if L[i][j] or L2[i][j]:
                ans += 1
    
    return ans

def main():
    H,W,N,M = map(int,input().split())
    AB,CD = [[False] * W for _ in range(H)],[[True] * W for _ in range(H)]
    for _ in range(N):
        a,b = map(int,input().split())
        AB[a-1][b-1] = True
    for _ in range(M):
        c,d = map(int,input().split())
        CD[c-1][d-1] = False
    
    print(solve(CD,AB,H,W))

if __name__ == "__main__":
    main()
