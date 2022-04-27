def comb(n,r,m):
    nume,deno = 1,1
    for i in range(1,r+1):
        nume *= (n-i+1)
        nume %= m
        deno *= i
        deno %= m

    output = (nume * inv(deno,m)) % m
    return output

def inv(a,p):
    return pow(a,p-2,p)

def main():
    W,H = map(int,input().split())
    M = 10**9+7

    ans = comb(W+H-2,min(W-1,H-1),M)

    print(ans)

if __name__ == "__main__":
    main()
