def move(LR,ST,N,D,K):
    Day = [None for _ in range(K)]

    for d in range(D):
        for k in range(K):
            S,T = ST[k][0],ST[k][1]
            if S == T and Day[k] == None:
                Day[k] = d
            else:
                L,R = LR[d][0],LR[d][1]
                if S < T and L <= S <= R:
                    ST[k][0] = min(T,R)
                if S > T and L <= S <= R:
                    ST[k][0] = max(T,L)

    for k in range(K):
        if Day[k] == None:
            Day[k] = D

    return Day

def main():
    N,D,K = map(int,input().split())
    LR = [list(map(int,input().split())) for _ in range(D)]
    ST = [list(map(int,input().split())) for _ in range(K)]

    ans = move(LR,ST,N,D,K)
    for i in range(K):
        print(ans[i])

if __name__ == "__main__":
    main()
