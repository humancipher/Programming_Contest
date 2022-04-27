from sys import stdin
from collections import deque
INF = 10**15
INF2 = 10**12
input = stdin.readline

def bfs(S,h,w,key,sx,sy,gx,gy):
    D = [[INF] * w for _ in range(h)]
    D[sx][sy] = 0
    V = [(0,1),(0,-1),(1,0),(-1,0)]
    Q = deque()
    Q.append([sx,sy,0])
    while len(Q) > 0:
        px,py,pt = Q.popleft()
        for vx,vy in V:
            if 0 <= px+vx < h and 0 <= py+vy < w:
                if S[px+vx][py+vy] == "#":
                    nexttime = pt + key
                else:
                    nexttime = pt + 1
                if D[px+vx][py+vy] > nexttime:
                    D[px+vx][py+vy] = nexttime
                    Q.append([px+vx,py+vy,nexttime])
    return D[gx][gy]

def bsearch(S,h,w,sx,sy,gx,gy,t):
    left,right = 1,INF2
    while right-left > 1:
        mid = (right+left)//2
        if bfs(S,h,w,mid,sx,sy,gx,gy) <= t:
            left = mid
        else:
            right = mid
    return left

def main():
    h,w,t = map(int,input().split())
    S = [input() for _ in range(h)]
    for i in range(h):
        for j in range(w):
            if S[i][j] == "S":
                sx,sy = i,j
            if S[i][j] == "G":
                gx,gy = i,j
    print(bsearch(S,h,w,sx,sy,gx,gy,t))

if __name__ == "__main__":
    main()
