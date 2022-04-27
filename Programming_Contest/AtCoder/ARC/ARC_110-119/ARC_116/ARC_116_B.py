mod = 998244353

def inv(n,mod):
    return pow(n,mod-2,mod)

def solve(A,N):
    if N == 1:
        return A[0]**2 % mod
    else:
        A.sort()
        B = [A[i] for i in range(1,N)] #B[i]:pow(2.i,mod)*A[i-1](i >= 1)
        pw = 1
        for i in range(N-1):
            B[i] *= pw
            B[i] %= mod
            pw *= 2
            pw %= mod
        C = [B[i] for i in range(N-1)]
        for i in range(1,N-1):
            C[i] += C[i-1]
            C[i] %= mod
        ans = 0
        inv2 = inv(2,mod)
        for i in range(N):
            ans += A[i]**2
            ans %= mod
        for i in range(N):
            if i == 0:
                tmp = C[N-2]
                ans += A[i] * tmp
                ans %= mod
            else:
                tmp -= A[i]
                tmp *= inv2
                tmp %= mod
                ans += A[i] * tmp
                ans %= mod
    return ans

def main():
    N = int(input())
    A = list(map(int,input().split()))
    print(solve(A,N))

if __name__ == "__main__":
    main()
