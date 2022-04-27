from queue import Queue

R,C = map(int,input().split())
sy,sx = map(int,input().split())
gy,gx = map(int,input().split())
D = [list(input()) for _ in range(R)]

def bfs(D,sy,sx,gy,gx):
    sy,sx,gy,gx = sy-1,sx-1,gy-1,gx-1
    Dist = [[None for _ in range(C)] for _ in range(R)]
    vec = [(-1,0),(1,0),(0,-1),(0,1)]
    q = Queue()
    q.put((sy,sx))
    Dist[sy][sx] = 0
    D[sy][sx] = "#"
    while not q.empty():
        p = q.get()
        py,px = p[0],p[1]
        if p == (gy,gx):
            return Dist[gy][gx]
        for vy,vx in vec:
            if D[py+vy][px+vx] == ".":
                q.put((py+vy,px+vx))
                Dist[py+vy][px+vx] = Dist[py][px]+1
                D[py+vy][px+vx] = "#"

ans = bfs(D,sy,sx,gy,gx)
print(ans)
