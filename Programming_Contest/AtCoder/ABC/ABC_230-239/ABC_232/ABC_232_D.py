from collections import deque

h,w = map(int,input().split())
C = [input() for _ in range(h)]
D = [[0] * w for _ in range(h)]
D[0][0] = 1
V = [(0,1),(1,0)]
ans = 1
Q = deque()
Q.append((0,0))
while len(Q) > 0:
    px,py = Q.popleft()
    for vx,vy in V:
        if px+vx < h and py+vy < w:
            if C[px+vx][py+vy] == "." and D[px+vx][py+vy] == 0:
                Q.append((px+vx,py+vy))
                D[px+vx][py+vy] = D[px][py] + 1
                ans = max(ans,D[px+vx][py+vy])
print(ans)