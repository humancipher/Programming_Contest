def prob(N,K):
    #(K以下,K,K以上)
    #(K,K,K)
    pat = 0
    pat += ((K-1) * (N-K)) * 3 * 2
    pat += (K-1) * 3
    pat += (N-K) * 3
    pat += 1

    return pat / N**3

def main():
    N,K = map(int,input().split())
    p = prob(N,K)
    print(p)

if __name__ == "__main__":
    main()
