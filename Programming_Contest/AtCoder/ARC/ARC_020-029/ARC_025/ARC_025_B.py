def main():
    import sys
    input = sys.stdin.readline
    h,w = map(int,input().split())
    C = [[0] * (w+1)]
    for _ in range(h):
        ci = list(map(int,input().split()))
        C.append([0] + ci)
    for i in range(h+1):
        for j in range(w+1):
            if (i+j) % 2 == 1:
                C[i][j] *= -1
    for i in range(h):
        for j in range(w+1):
            C[i+1][j] += C[i][j]
    for j in range(w):
        for i in range(h+1):
            C[i][j+1] += C[i][j]
    ans = 0
    for sx in range(1,h+1):
        for sy in range(1,w+1):
            for gx in range(sx,h+1):
                for gy in range(sy,w+1):
                    if C[gx][gy] == C[sx-1][gy] + C[gx][sy-1] - C[sx-1][sy-1]:
                        ans = max(ans,(gx-sx+1)*(gy-sy+1))
    print(ans)

if __name__ == "__main__":
    main()