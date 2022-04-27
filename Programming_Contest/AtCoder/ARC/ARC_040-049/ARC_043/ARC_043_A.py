def main():
    N,A,B = map(int,input().split())
    S = [int(input()) for _ in range(N)]

    max_S,min_S = max(S),min(S)
    if max_S == min_S:
        print(-1)
    else:
        sum_S = sum(S)
        P = B/(max_S-min_S)
        sum_S *= P
        Q = A - sum_S/N
        print(P,Q)

if __name__ == "__main__":
    main()
