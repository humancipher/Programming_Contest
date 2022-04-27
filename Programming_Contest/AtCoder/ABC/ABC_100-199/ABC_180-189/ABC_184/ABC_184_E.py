from collections import deque #データ構造キューはCollectionsから使うと速いらしい
INF = 1 << 25 #大きすぎると何度も見るときに重くなる

def solve(A,H,W):
    pad = ["#"*(W+2)]
    for i in range(H):
        A[i] = "#" + A[i] + "#"
    A = pad + A + pad
    H += 2
    W += 2
    D = [[INF] * W for _ in range(H)] #D[i][j]==INFなら(i,j)は未訪問、違うなら最小コスト確定
    WP = [set() for _ in range(26)] #"a","b",...のワープポイント
    Use = [True for _ in range(26)] # i番目のワープポイントが未使用かどうか
    for i in range(1,H-1):
        for j in range(1,W-1):
            if A[i][j] == "#" or A[i][j] == ".":
                continue
            elif A[i][j] == "S":
                D[i][j] = 0
                sy,sx = i,j
            elif A[i][j] == "G":
                gy,gx = i,j
            else:
                WP[ord(A[i][j])-97].add((i,j))
    q = deque()
    q.append((sy,sx))
    V = [(0,1),(0,-1),(1,0),(-1,0)]
    while q:
        (py,px) = q.popleft()
        if ord("a") <= ord(A[py][px]) <= ord("z"):
            alf = ord(A[py][px])-ord("a")
            if Use[alf]:
                Use[alf] = False
                for (y,x) in WP[alf]:
                    if D[y][x] == INF:
                        q.append((y,x))
                        D[y][x] = D[py][px] + 1
        for (vy,vx) in V:
            if A[py+vy][px+vx] != "#" and D[py+vy][px+vx] == INF:
                q.append((py+vy,px+vx))
                D[py+vy][px+vx] = D[py][px] + 1

    if D[gy][gx] == INF:
        return -1 #最後まで(gy,gx)が未訪問
    else:
        return D[gy][gx]

def main():
    H,W = map(int,input().split())
    A = [input() for _ in range(H)]
    print(solve(A,H,W))

if __name__ == "__main__":
    main()
