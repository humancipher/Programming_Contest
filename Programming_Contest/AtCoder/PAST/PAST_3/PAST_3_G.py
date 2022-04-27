from queue import Queue

def bfs(S,gx,gy):
    INF = 10**5
    D = [[INF for _ in range(403)] for _ in range(403)]
    D[201][201] = 0
    Q = Queue()
    Q.put([201,201])
    V = [[1,1],[0,1],[-1,1],[1,0],[-1,0],[0,-1]]

    while not Q.empty():
        p = Q.get()
        px,py = p[0],p[1]
        S[px][py] = "B"
        if px == gx and py == gy:
            return D[gx][gy]
        else:
            for vx,vy in V:
                if 0 <= px+vx <= 402 and 0 <= py+vy <= 402:
                    if S[px+vx][py+vy] == "W":
                        Q.put([px+vx,py+vy])
                        S[px+vx][py+vy] = "B"
                        D[px+vx][py+vy] = D[px][py] + 1
    return -1

def main():
    N,X,Y = map(int,input().split())
    xy = [list(map(int,input().split())) for _ in range(N)]

    for i in range(N):
        xy[i][0] += 201
        xy[i][1] += 201
    X += 201
    Y += 201

    #B:通過不能,W:通過可能
    S = [["W" for _ in range(403)] for _ in range(403)]
    for i in range(N):
        x,y = xy[i][0],xy[i][1]
        S[x][y] = "B"

    print(bfs(S,X,Y))

if __name__ == "__main__":
    main()
