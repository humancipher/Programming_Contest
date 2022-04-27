def Reverse(S,H,W):
    for i in range(H):
        S[i] = "#" + S[i] + "#"
    S = ["#"*(W+2)] + S + ["#"*(W+2)]

    V = [(0,0),(0,1),(0,-1),(1,0),(1,-1),(1,1),(-1,0),(-1,1),(-1,-1)]
    Rev_black = set() #復元したときに黒になる点
    for i in range(1,H+1):
        for j in range(1,W+1):
            black = True
            for vh,vw in V:
                if S[i+vh][j+vw] == ".":
                    black = False
                    break
            if black:
                Rev_black.add((i,j))

    can = True
    for i in range(1,H+1):
        for j in range(1,W+1):
            if S[i][j] == "#":
                check = False
                for vh,vw in V:
                    if (i+vh,j+vw) in Rev_black:
                        check = True
                        break
                if not check:
                    can = False
                    break
        if not can:
            break

    if not can:
        return (False,None)
    else:
        T = []
        for i in range(1,H+1):
            t = ""
            for j in range(1,W+1):
                if (i,j) in Rev_black:
                    t += "#"
                else:
                    t += "."
            T.append(t)
        return (True,T)

def main():
    H,W = map(int,input().split())
    S = [input() for _ in range(H)]

    ans = Reverse(S,H,W)
    if ans[0]:
        print("possible")
        for i in range(len(ans[1])):
            print(ans[1][i])
    else:
        print("impossible")

if __name__ == "__main__":
    main()
