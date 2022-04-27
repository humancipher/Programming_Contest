#枝刈りbfs
from collections import deque
import sys
input = sys.stdin.readline
INF = 10**7

def bfs(S,h2,w2,sx,sy,gx,gy):
    VX = [0,1,0,-1]
    VY = [1,0,-1,0]
    D = [[INF] * w2 for _ in range(h2)]
    #D[i][j]:マス(i,j)にくるまでに向きを替えた回数(止まったところから動くのも変更1回)
    Q = deque()
    D[sx][sy] = -1
    Q.append((sx,sy))
    while Q:
        px,py = Q.popleft()
        ncost = D[px][py]+1
        for vx,vy in zip(VX,VY):
            nx,ny = px+vx,py+vy
            while S[nx][ny] == ".":
                if D[nx][ny] > ncost:
                    D[nx][ny] = ncost
                    Q.append((nx,ny))
                elif D[nx][ny] < ncost:
                    break
                nx += vx
                ny += vy
    D[sx][sy] = 0
    return D[gx][gy]

def main():
    h,w = map(int,input().split())
    h2,w2 = h+2,w+2
    sx,sy = map(int,input().split())
    gx,gy = map(int,input().split())
    #壁で埋めて枠の判定を不要にする
    S = ["#" * (w2)]
    S.extend("#" + input().rstrip() + "#" for _ in range(h))
    S.append("#" * (w2))
    
    print(bfs(S,h2,w2,sx,sy,gx,gy))

if __name__ == "__main__":
    main()