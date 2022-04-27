INF = 2501

def solve(A,N):
    taka_ans = -INF
    for i in range(N): #高橋の選択
        taka_tmp = 0
        taka,aoki = 0,0
        aoki_max = -INF
        for j in range(N): #青木の選択
            if i == j:
                continue
            else:
                taka,aoki = 0,0
                for k in range(min(i,j),max(i,j)+1):
                    if (k - min(i,j)) % 2 == 0:
                        taka += A[k]
                    else:
                        aoki += A[k]
                if aoki_max < aoki:
                    aoki_max = aoki
                    taka_tmp = taka
        taka_ans = max(taka_ans,taka_tmp)
    return taka_ans

def main():
    N = int(input())
    A = list(map(int,input().split()))
    print(solve(A,N))

if __name__ == "__main__":
    main()
