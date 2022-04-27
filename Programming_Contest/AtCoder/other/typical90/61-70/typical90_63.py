h,w = map(int,input().split())
P = [list(map(int,input().split())) for _ in range(h)]

ans = 0
F = [-1 for _ in range(w)] #j列目で使う数
G = [1 for _ in range(w)] #j列目が選んだ行で全部一致しているかどうか
for b in range(2**h):
    first = True
    hw = 0
    for i in range(h):
        if 2**i & b != 0:
            hw += 1
            if first:
                first = False
                for j in range(w):
                    F[j] = P[i][j]
                    G[j] = 1
            else:
                for j in range(w):
                    if F[j] != P[i][j]:
                        G[j] = 0
    M = dict()
    yoko = 0
    for j in range(w):
        if G[j] == 1:
            if F[j] in M:
                M[F[j]] += 1
            else:
                M[F[j]] = 1
    for m in M:
        yoko = max(yoko,M[m])
    ans = max(ans,hw * yoko)
print(ans)