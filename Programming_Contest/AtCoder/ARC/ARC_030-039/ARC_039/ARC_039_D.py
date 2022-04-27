mod = 10**9+7

def comb(n,k,mod):
    bunsi = 1
    bunbo = 1
    for i in range(k):
        bunsi *= n-i
        bunsi %= mod
        bunbo *= i+1
        bunbo %= mod
    return (bunsi * pow(bunbo,mod-2,mod)) % mod

def main():
    n,k = map(int,input().split())
    amari = k % n
    if n > k:
        print(comb(n+k-1,k,mod))
    else:
        print(comb(n,amari,mod))

if __name__ == "__main__":
    main()
