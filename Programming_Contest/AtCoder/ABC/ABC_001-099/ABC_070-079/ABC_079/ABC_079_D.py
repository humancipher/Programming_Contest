def shortpath(C):
    #魔力表Cの任意のパスを最小化したい
    update = True
    while update:
        update = False
        for i in range(10):
            for j in range(10):
                for k in range(10):
                    if C[i][j] > C[i][k] + C[k][j]:
                        C[i][j] = C[i][k] + C[k][j]
                        update = True
    return C

def main():
    H,W = map(int,input().split())
    C = [list(map(int,input().split())) for _ in range(10)]
    A = [list(map(int,input().split())) for _ in range(H)]

    C = shortpath(C)
    ans = 0
    for i in range(H):
        for j in range(W):
            if abs(A[i][j]) != 1:
                ans += C[A[i][j]][1]

    print(ans)

if __name__ == "__main__":
    main()
