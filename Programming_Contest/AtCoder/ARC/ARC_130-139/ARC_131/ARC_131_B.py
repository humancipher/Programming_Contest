h,w = map(int,input().split())
C = [list(input()) for _ in range(h)]

V = [(0,1),(0,-1),(1,0),(-1,0)]

Kouho = [[set([str(x) for x in range(1,6)]) for _ in range(w)] for _ in range(h)]

for i in range(h):
    for j in range(w):
        if C[i][j] == ".":
            for vx,vy in V:
                if 0 <= i+vx < h and 0 <= j+vy < w:
                    Kouho[i][j].discard(C[i+vx][j+vy])
            Kouho[i][j] = list(Kouho[i][j])
            C[i][j] = Kouho[i][j][0]
            Kouho[i][j] = set(Kouho[i][j])
        else:
            for vx,vy in V:
                if 0 <= i+vx < h and 0 <= j+vy < w:
                    Kouho[i+vx][j+vy].discard(C[i][j])

for i in range(h):
    print("".join(C[i]))