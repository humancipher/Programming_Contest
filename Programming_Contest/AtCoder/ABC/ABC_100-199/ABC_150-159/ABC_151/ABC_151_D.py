import queue

H,W = map(int,input().split())
S = [list(input()) for _ in range(H)]
INF = H*W+1

def movable(S,S_dist,px,py):
    if  0 <= px and px < H and 0 <= py and py < W:
        if S_dist[px][py] == INF and S[px][py] == ".":
            return True
    return False

def bfs(S,sx,sy):
    S_dist = [[INF for _ in range(W)] for _ in range(H)]
    #Sを直接いじれば訪問済みかどうか管理できるがそれだと毎回Sをリセットする必要がある
    #S_distのみ書き込みにすればS_distはローカルだからリセットが不要
    S_dist[sx][sy] = 0
    q = queue.Queue()
    q.put((sx,sy))
    vec = [(0,1),(0,-1),(1,0),(-1,0)]
    ret = 0
    while not q.empty():
        p = q.get()
        ret = S_dist[p[0]][p[1]]
        for vx,vy in vec:
            if movable(S,S_dist,p[0]+vx,p[1]+vy):
                S_dist[p[0]+vx][p[1]+vy] = S_dist[p[0]][p[1]]+1
                q.put((p[0]+vx,p[1]+vy))
    return ret

ans = 0
for i in range(H*W):
    if S[i//W][i%W] == ".":
        ans = max(ans,bfs(S,i//W,i%W))
print(ans)
