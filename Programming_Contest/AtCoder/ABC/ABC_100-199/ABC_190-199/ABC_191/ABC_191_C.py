def solve(S,H,W):
    ans = 0
    for i in range(H-1):
        for j in range(W-1):
            tmp = 0
            for v in [(0,0),(0,1),(1,0),(1,1)]:
                if S[i+v[0]][j+v[1]] == "#":
                    tmp += 1
            if tmp == 1 or tmp == 3:
                ans += 1
    return ans

def main():
    H,W = map(int,input().split())
    S = [input() for _ in range(H)]
    print(solve(S,H,W))

if __name__ == "__main__":
    main()
