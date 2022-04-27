from collections import deque
from sys import stdin
input = stdin.readline
INF = 10**6

def main():
    V = [(0,1),(0,-1),(1,0),(-1,0)]
    r,c,k = map(int,input().split())
    S = [input() for _ in range(r)]
    D = [[INF] * c for _ in range(r)]
    Q = deque()

    for i in range(r):
        for j in range(c):
            if S[i][j] == "x":
                Q.append([i,j,0])
                D[i][j] = 0

    #黒マスとの距離の最小値を計算
    while len(Q) > 0:
        x,y,z = Q.popleft()
        for vx,vy in V:
            if 0 <= x+vx < r and 0 <= y+vy < c:
                if D[x+vx][y+vy] > z+1:
                    Q.append([x+vx,y+vy,z+1])
                    D[x+vx][y+vy] = z+1
    
    #壁との距離の最小値を計算
    for i in range(r):
        for j in range(c):
            D[i][j] = min(D[i][j],min(i,j,r-1-i,c-1-j)+1)
    
    ans = 0
    for i in range(r):
        for j in range(c):
            if D[i][j] >= k:
                ans += 1
    print(ans)

if __name__ == "__main__":
    main()
