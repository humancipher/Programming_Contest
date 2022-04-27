def Divisors(n):
    d = 1
    Ans = set()
    while d ** 2 <= n:
        if n % d == 0:
            Ans.add(d)
            Ans.add(n // d)
        d += 1
    return Ans

def solve(N):
    Div = Divisors(2 * N)
    ans = 0
    for d in Div:
        if (2 * N // d - d - 1) % 2 == 0:
            ans += 1
    return ans

def main():
    N = int(input())
    
    print(solve(N))

if __name__ == "__main__":
    main()
