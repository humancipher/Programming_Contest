from collections import deque

INF = 10**7

def bfs(A,h,w):
    V = [(0,1),(0,-1),(1,0),(-1,0)]
    D = [[INF] * w for _ in range(h)]
    Q = deque()
    for i in range(h):
        for j in range(w):
            if A[i][j] == "#":
                D[i][j] = 0
                Q.append([i,j])
    while len(Q) > 0:
        [px,py] = Q.popleft()
        for vx,vy in V:
            if 0 <= px+vx < h and 0 <= py+vy < w:
                if D[px+vx][py+vy] == INF:
                    Q.append([px+vx,py+vy])
                    D[px+vx][py+vy] = D[px][py] + 1
    ans = 0
    for i in range(h):
        for j in range(w):
            if A[i][j] == ".":
                ans = max(ans,D[i][j])
    return ans

def main():
    h,w = map(int,input().split())
    A = [input() for _ in range(h)]
    print(bfs(A,h,w))

if __name__ == "__main__":
    main()
