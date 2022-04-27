def mov(xy,N):
    Box_red = set([1])
    Box = [1 for _ in range(N)]

    for i in range(len(xy)):
        Box[xy[i][0]-1] -= 1
        Box[xy[i][1]-1] += 1
        if xy[i][0] in Box_red:
            Box_red.add(xy[i][1])
        if Box[xy[i][0]-1] == 0:
            Box_red.discard(xy[i][0])

    return len(Box_red)

def main():
    N,M = map(int,input().split())
    xy = [list(map(int,input().split())) for _ in range(M)]
    ans = mov(xy,N)
    print(ans)

if __name__ == "__main__":
    main()
