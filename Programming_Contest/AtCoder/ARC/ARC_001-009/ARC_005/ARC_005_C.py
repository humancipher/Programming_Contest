from heapq import heapify,heappop,heappush
INF = 2501

def main():
    import sys
    input = sys.stdin.readline
    h,w = map(int,input().split())
    C = [input().rstrip() for _ in range(h)]
    for i in range(h):
        for j in range(w):
            if C[i][j] == "s":
                sx,sy = i,j
            if C[i][j] == "g":
                gx,gy = i,j
    D = [[INF] * w for _ in range(h)]
    D[sx][sy] = 0
    V = [(0,1),(0,-1),(1,0),(-1,0)]
    HQ = []
    heapify(HQ)
    heappush(HQ,(0,sx,sy))
    while len(HQ) > 0 and D[gx][gy] > 2:
        now,px,py = heappop(HQ)
        if now > 2:
            break
        for vx,vy in V:
            if 0 <= px+vx and px+vx < h and 0 <= py+vy and py+vy < w:
                diff = 0
                if C[px+vx][py+vy] == "#":
                    diff = 1
                if D[px+vx][py+vy] > now + diff:
                    D[px+vx][py+vy] = now + diff
                    heappush(HQ,(now+diff,px+vx,py+vy))
    if D[gx][gy] <= 2:
        print("YES")
    else:
        print("NO")

if __name__ == "__main__":
    main()
