from collections import deque
import sys

sys.setrecursionlimit(500005)
stdin = sys.stdin

"""
ni = lambda: int(ns())
na = lambda: list(map(int, stdin.readline().split()))
ns = lambda: stdin.readline().strip()

h, w = na()
b = []
for i in range(h):
    b.append(ns())
"""
h,w = 2000,2000
b = [["."] * w for _ in range(h)]
b[0][0] = "S"
b[h-1][h-1] = "G"
for i in range(h):
    b[i] = "".join(b[i])
sr, sc = 0, 0
gr, gc = 0, 0
portals = [[] for _ in range(26)]

for i in range(h):
    for j in range(w):
        if b[i][j] == "S":
            sr, sc = i, j
        if b[i][j] == "G":
            gr, gc = i, j
        if ord("z") >= ord(b[i][j]) >= ord("a"):
            portals[ord(b[i][j])-ord("a")].append((i, j))
q = deque()

ds = [999999999999] * (h*w+26)
q.append(sr*w+sc)
ds[sr*w+sc] = 0
dx = ((1, 0), (0, 1), (-1, 0), (0, -1))
while q:
    cur = q.popleft()
    if cur < h*w:
        r = cur//w
        c = cur%w
        for t in dx:
            nr, nc = r + t[0], c + t[1]
            if 0 <= nr < h and 0 <= nc < w and b[nr][nc] != "#" and ds[nr*w+nc] > ds[cur] + 1:
                ds[nr * w + nc] = ds[cur] + 1
                q.append(nr*w+nc)
        if ord("z") >= ord(b[r][c]) >= ord("a"):
            ind = ord(b[r][c])-ord("a")
            if ds[h*w+ind] > ds[cur] + 1:
                ds[h*w+ind] = ds[cur] + 1
                q.append(h*w+ind)
    else:
        for t in portals[cur-h*w]:
            if ds[t[0]*w+t[1]] > ds[cur]:
                ds[t[0] * w + t[1]] = ds[cur]
                q.appendleft(t[0] * w + t[1])
print(ds[gr*w+gc] if ds[gr*w+gc] <= 4000000 else -1)
