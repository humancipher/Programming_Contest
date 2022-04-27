def dist(a,b):
    return abs(a[0]-b[0]) + abs(a[1]-b[1])

def solve(XY,n,Q,q):
    x0,y0 = XY[0][0],XY[0][1]
    x1,y1 = XY[0][0],XY[0][1]
    for x,y in XY:
        x0,y0 = min(x0,x),min(y0,y)
        x1,y1 = max(x1,x),max(y1,y)
    D,P = [0,0,0,0],[0,0,0,0] #マンハッタン距離が最大になりそうな点を調べる
    S = [[x0,y0],[x0,y1],[x1,y0],[x1,y1]]
    for i in range(n):
        for j in range(4):
            if dist(XY[i],S[j]) > D[j]:
                D[j] = dist(XY[i],S[j])
                P[j] = i
    Ans = []
    for i in range(q):
        ans = 0
        for j in range(4):
            ans = max(ans,dist(XY[Q[i]-1],XY[P[j]]))
        Ans.append(ans)
    return Ans

def main():
    n,q = map(int,input().split())
    XY = [list(map(int,input().split())) for _ in range(n)]
    Q = [int(input()) for _ in range(q)]
    Ans = solve(XY, n, Q, q)
    for i in range(q):
        print(Ans[i])

if __name__ == "__main__":
    main()
