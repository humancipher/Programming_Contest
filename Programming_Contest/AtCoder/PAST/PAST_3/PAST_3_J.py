from bisect import bisect_left

def eat(a,M,N):
    H = [0 for _ in range(N)]
    #H[i]:N-i番目の子がたべた最もおいしい寿司のおいしさ
    C = [0 for _ in range(N)]
    #C[i]:N-i番目の子が食べた寿司の個数
    #このルールだと常にi<j なら H[i] <= H[j]になる
    for i in range(M):
        eater = bisect_left(H,a[i])
        if eater > 0:
            C[eater-1] += 1
            H[eater-1] = a[i]
            print(N-eater+1)
        else:
            print(-1)

def main():
    N,M = map(int,input().split())
    a = list(map(int,input().split()))

    eat(a,M,N)

if __name__ == "__main__":
    main()
