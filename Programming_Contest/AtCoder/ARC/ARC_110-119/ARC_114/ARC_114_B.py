mod = 998244353

def solve(F,N):
    pro = 0
    Use = [False for _ in range(N+1)]
    Tmp = set()
    for i in range(1,N+1):
        Tmp.clear()
        if not Use[i]:
            Tmp.add(i)
            Use[i] = True
            a = F[i]
            while not Use[a]:
                Tmp.add(a)
                Use[a] = True
                a = F[a]
            if a in Tmp:
                pro += 1
    ans = pow(2,pro,mod)
    ans -= 1
    ans %= mod
    return ans

def main():
    N = int(input())
    F = list(map(int,input().split()))
    F = [0] + F
    print(solve(F,N))

if __name__ == "__main__":
    main()
