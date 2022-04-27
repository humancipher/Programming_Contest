def TS(G,v,e):
    INF = 16000
    DP = [[INF for _ in range(v)] for _ in range(2**v)]
    #DP[i][j]:訪問済みエリアのリストがiでjにいるような最短距離
    DP[0][0] = 0
    #   どれも訪問してない状態は00...0(長さv)として訪問済みを表現
    for i in range(2**v):
        for j in range(v):
            for k in range(v):
                if i ^ 2**k < i and j != k \
                and DP[i ^ 2**k][k] + G[k][j] < DP[i][j]:
                    DP[i][j] = DP[i ^ 2**k][k] + G[k][j]

    if DP[2**v-1][0] != INF:
        return DP[2**v-1][0]
    else:
        return -1

def main():
    v,e = map(int,input().split())
    INF = 16000
    G = [[INF for _ in range(v)] for _ in range(v)]
    for i in range(e):
        s,t,d = map(int,input().split())
        G[s][t] = d

    print(TS(G,v,e))

if __name__ == "__main__":
    main()
