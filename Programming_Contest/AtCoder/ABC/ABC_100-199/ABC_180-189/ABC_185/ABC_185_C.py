def kaijo(n):
    ans = 1
    for i in range(2,n+1):
        ans *= i
    return ans

def comb(n,k):
    return kaijo(n) //(kaijo(k) * kaijo(n-k))

def main():
    L = int(input())
    print(comb(L-1,11))

if __name__ == "__main__":
    main()
