def cal(S,N,K,M,R):
    if N == 1:
        return R
    elif K == 1:
        if max(S) >= R:
            return 0
        else:
            return R
    else:
        S.append(0)
        S.sort(reverse=True)
        for i in range(1,N):
            S[i] += S[i-1]
        if S[K-1] >= R*K:
            return 0
        else:
            if R*K - S[K-2] <= M:
                return R*K - S[K-2]
            else:
                return -1

def main():
    N,K,M,R = map(int,input().split())
    S = [int(input()) for _ in range(N-1)]

    print(cal(S,N,K,M,R))

if __name__ == "__main__":
    main()
