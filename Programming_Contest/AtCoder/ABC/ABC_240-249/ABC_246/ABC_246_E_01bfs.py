from collections import deque
from sys import stdin
input = stdin.readline
INF = (1 << 62) - 1

#01bfs
def exbfs(S,n2,ax,ay,bx,by):
    V = [(1,1),(1,-1),(-1,1),(-1,-1)]
    D = [[[INF] * 4 for _ in range(n2)] for _ in range(n2)]
    Q = deque()
    for i in range(4):
        Q.append((ax,ay,i,1))
        D[ax][ay][i] = 1
    while Q:
        px,py,muki,dist = Q.popleft()
        if dist > D[px][py][muki]:
            continue
        for i in range(4):
            nx,ny = px+V[i][0],py+V[i][1]
            if muki == i:
                if S[nx][ny] == "." and dist < D[nx][ny][i]:
                    Q.appendleft((nx,ny,i,dist))
                    D[nx][ny][i] = dist
            else:
                if S[nx][ny] == "." and dist+1 < D[nx][ny][i]:
                    Q.append((nx,ny,i,dist+1))
                    D[nx][ny][i] = dist+1
    for i in range(4):
        D[ax][ay][i] = 0
    return min(D[bx][by])

def main():
    n = int(input())
    n2 = n+2
    ax,ay = map(int,input().split())
    bx,by = map(int,input().split())
    # 周辺を壁で埋めて、判定を楽にします
    S = ["#" * n2]
    S.extend("#" + input().rstrip() + "#" for _ in range(n))
    S.append("#" * n2)
    ans = exbfs(S,n2,ax,ay,bx,by)
    if ans == INF:
        print(-1)
    else:
        print(ans)

if __name__ == "__main__":
    main()
