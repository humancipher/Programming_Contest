def train_map(LR,N):
    train = [[0 for _ in range(N+1)] for _ in range(N+1)]
    #train[i][j]:ちょうど区間iからjを走る電車の本数（後に累積和に）
    for l,r in LR:
        train[l][r] += 1

    #累積和
    for i in range(N+1):
        for j in range(1,N+1):
            train[i][j] += train[i][j-1]
    for j in range(N+1):
        for i in reversed(range(1,N+1)):
            train[i-1][j] += train[i][j]

    return train

def main():
    N,M,Q = list(map(int,input().split()))
    LR = [list(map(int,input().split())) for _ in range(M)]
    pq = [list(map(int,input().split())) for _ in range(Q)]

    train = train_map(LR,N)

    for p,q in pq:
        print(train[p][q])

if __name__ == "__main__":
    main()
