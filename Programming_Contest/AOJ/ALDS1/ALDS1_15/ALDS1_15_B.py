def main():
    N,W = map(int,input().split())
    vw = [list(map(int,input().split())) for _ in range(N)]

    for i in range(N):
        vw[i].append(vw[i][0]/vw[i][1])

    vw.sort(reverse = True,key = lambda x:x[2])

    val,wei = 0,0
    for i in range(N):
        if wei + vw[i][1] <= W:
            val += vw[i][0]
            wei += vw[i][1]
        elif wei < W:
            val += vw[i][0]*(W-wei)/vw[i][1]
            wei = W
        else:
            break
    print(val)

if __name__ == "__main__":
    main()
