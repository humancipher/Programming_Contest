from queue import Queue

INF = 1 << 60

def solve(S,sx,sy,gx,gy,H,W):
    D = [[INF for _ in range(W)] for _ in range(H)]
    D[sy][sx] = 0
    Q = Queue()
    Q.put((sy,sx))

    Visit,Next_Visit = set(),set()
    while True:
        Visit.clear()
        for nv in Next_Visit:
            Visit.add(nv)
        
        while not Q.empty():
            py,px = Q.get()
            Visit.add((py,px))
            for x in {-1,0,1}: #歩き
                for y in {-1,0,1}:
                    if  abs(x) + abs(y) == 1:
                        if S[py+y][px+x] != "#":
                            if D[py+y][px+x] > D[py][px]:
                                D[py+y][px+x] = D[py][px]
                                Q.put((py+y,px+x))
                                Visit.add((py+y,px+x))
                                if py+y == gy and px+x == gx:
                                    return D[py+y][px+x]
        
        Next_Visit.clear()
        for py,px in Visit:
            for x in {-2,-1,0,1,2}: #ワープ
                for y in {-2,-1,0,1,2}:
                    if S[py+y][px+x] != "#":
                        if D[py+y][px+x] > D[py][px] + 1:
                            D[py+y][px+x] = D[py][px] + 1
                            Q.put((py+y,px+x))
                            Next_Visit.add((py+y,px+x))
        
        if len(Next_Visit) == 0:
            break
    
    return D[gy][gx]

def main():
    H,W = map(int,input().split())
    sy,sx = map(int,input().split())
    gy,gx = map(int,input().split())
    S = [input() for _ in range(H)]
    for i in range(H):
        S[i] = "##" + S[i] + "##"
    S = ["#"*(W+4)] * 2 + S + ["#"*(W+4)] * 2

    ans = solve(S,sx+1,sy+1,gx+1,gy+1,H+4,W+4)
    if ans != INF:
        print(ans)
    else:
        print(-1)

if __name__ == "__main__":
    main()
