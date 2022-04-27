def cal(XL):
    N = len(XL)
    XL.sort(key = lambda x:x[0])
    for i in range(N):
        XL[i] = [XL[i][0],XL[i][0]-XL[i][1],XL[i][0]+XL[i][1]]
    OP = [XL[0]]

    for i in range(1,N):
        if OP[len(OP)-1][2] > XL[i][1]:
            if OP[len(OP)-1][2] < XL[i][2]:
                #右方向により腕が伸びている方がより邪魔
                pass
            else:
                OP.pop()
                OP.append(XL[i])
        else:
            OP.append(XL[i])

    return len(OP)

def main():
    N = int(input())
    XL = [list(map(int,input().split())) for _ in range(N)]
    ans = cal(XL)
    print(ans)

if __name__ == "__main__":
    main()
