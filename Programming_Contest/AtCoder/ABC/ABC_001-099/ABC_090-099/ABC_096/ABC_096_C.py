def solve(S,H,W):
    for i in range(H):
        S[i] = "." + S[i] + "."
    S = ["." * (W+2)] + S + ["." * (W+2)]

    for i in range(1,H+1):
        for j in range(1,W+1):
            if not judge(S,i,j):
                return False

    return True

def judge(S,h,w):
    V = [(-1,0),(1,0),(0,-1),(0,1)]
    if S[h][w] == ".":
        return True
    else:
        for vh,vw in V:
            if S[h+vh][w+vw] == "#":
                return True
        return False

def main():
    H,W = map(int,input().split())
    S = [input() for _ in range(H)]

    if solve(S,H,W):
        print("Yes")
    else:
        print("No")

if __name__ == "__main__":
    main()
