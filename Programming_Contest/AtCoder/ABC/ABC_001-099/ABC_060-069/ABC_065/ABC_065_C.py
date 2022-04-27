def fact(n,mod):
    ans = 1
    for i in range(2,n+1):
        ans *= i
        ans %= mod
    return ans

def solve(n,m):
    if abs(n-m) >= 2:
        return 0
    else:
        mod = 10**9+7
        if n == m:
            return (2 * fact(n,mod)**2) % mod
        else:
            return (fact(n,mod) * fact(m,mod)) % mod

def main():
   n,m = map(int,input().split())
   print(solve(n,m))

if __name__ == "__main__":
    main()
