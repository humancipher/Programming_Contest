def main():
    N = int(input())
    T = [int(input()) for _ in range(N)]

    M = 10**9+7

    T.sort(reverse = True)

    pena = 0
    for i in range(N):
        pena += T[i] * (i+1)

    T_set = set()
    for i in range(N):
        if T[i] not in T_set:
            T_set.add(T[i])

    Col = []
    for t in T_set:
        tc = T.count(t)
        if tc > 1:
            Col.append(tc)

    pat = 1
    for i in range(len(Col)):
        for j in range(2,Col[i]+1):
            pat *= j
            pat %= M

    print(pena)
    print(pat)

if __name__ == "__main__":
    main()
