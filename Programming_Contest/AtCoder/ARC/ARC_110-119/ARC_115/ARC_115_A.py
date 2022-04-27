def comb(m,n):
    bunsi,bunbo = 1,1
    for i in range(1,n+1):
        bunsi *= m-i+1
        bunbo *= i
    return bunsi // bunbo

def hw(S):
    return S.count("1")

def solve(S,N,M):
    H = [0 for _ in range(M+1)]
    for s in S:
        H[hw(s)] += 1
    even,odd = 0,0
    for i in range(M+1):
        if i % 2 == 0:
            even += H[i]
        else:
            odd += H[i]
    ans = comb(N,2)
    if even >= 2:
        ans -= comb(even,2)
    if odd >= 2:
        ans -= comb(odd,2)
    return ans

def main():
    N,M = map(int,input().split())
    S = [input() for _ in range(N)]
    print(solve(S,N,M))

if __name__ == "__main__":
    main()
