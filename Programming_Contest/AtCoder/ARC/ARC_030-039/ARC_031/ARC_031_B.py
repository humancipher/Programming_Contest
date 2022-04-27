from collections import deque
from sys import stdin
input = stdin.readline

def main():
    n = 10
    A = [list(input().rstrip()) for _ in range(n)]
    B = [[None] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if A[i][j] == "x":
                B[i][j] = 0
    cnt = 1
    V = [(0,1),(0,-1),(1,0),(-1,0)]
    Q = deque()
    
    for i in range(n):
        for j in range(n):
            if A[i][j] == "o" and B[i][j] == None:
                Q.append((i,j))
                B[i][j] = cnt
                while Q:
                    x,y = Q.popleft()
                    for vx,vy in V:
                        if 0 <= x+vx and x+vx < n and 0 <= y+vy and y+vy < n:
                            if A[x+vx][y+vy] == "o" and B[x+vx][y+vy] == None:
                                Q.append((x+vx,y+vy))
                                B[x+vx][y+vy] = B[x][y]
                cnt += 1
    S = [set() for _ in range(n**2)]
    for i in range(n):
        for j in range(n):
            if B[i][j] != 0:
                S[B[i][j]-1].add((i,j))
    if cnt == 2:
        ans = "YES"
    else:
        flag = False
        for i in range(n):
            for j in range(n):
                D = [n**2] * (cnt-1)
                for vx,vy in V:
                    if 0 <= i+vx and i+vx < n and 0 <= j+vy and j+vy < n:
                        if B[i+vx][j+vy] != 0:
                            D[B[i+vx][j+vy]-1] = 1
                if max(D) == 1:
                    flag = True
                    break
        if flag:
            ans = "YES"
        else:
            ans = "NO"                
    print(ans)

if __name__ == "__main__":
    main()
