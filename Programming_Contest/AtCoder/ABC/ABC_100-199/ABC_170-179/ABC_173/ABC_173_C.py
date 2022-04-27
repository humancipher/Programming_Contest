def solve(C,H,W,tate,yoko,sum):
    for h in range(H):
        if 2**h & tate != 0:
            for w in range(W):
                if C[h][w] == "#":
                    sum -= 1

    for w in range(W):
        if 2**w & yoko != 0:
            for h in range(H):
                if C[h][w] == "#":
                    sum -= 1

    for h in range(H):
        for w in range(W):
            if 2**h & tate != 0 and 2**w & yoko != 0 and C[h][w] == "#":
                sum += 1

    return sum

def main():
    H,W,K = map(int,input().split())
    C = [input() for _ in range(H)]

    sum,ans = 0,0
    for h in range(H):
        for w in range(W):
            if C[h][w] == "#":
                sum += 1

    for i in range(2**H):
        for j in range(2**W):
            if solve(C,H,W,i,j,sum) == K:
                ans += 1

    print(ans)

if __name__ == "__main__":
    main()
