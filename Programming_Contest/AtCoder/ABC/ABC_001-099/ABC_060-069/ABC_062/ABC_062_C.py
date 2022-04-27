def solve(H,W):
    if H % 3 == 0 or W % 3 == 0:
        return 0
    else:
        pat1 = abs(H//3 * W - (H - H//3) * (W - W//2))
        pat2 = abs((H//3+1) * W - (H - H//3 - 1) * (W//2))
        pat3 = abs(W//3 * H - (W - W//3) * (H - H//2))
        pat4 = abs((W//3+1) * H - (W - W//3 - 1) * (H//2))
        return min(pat1,pat2,pat3,pat4,H,W)

def main():
    H,W = map(int,input().split())
    print(solve(H,W))

if __name__ == "__main__":
    main()
