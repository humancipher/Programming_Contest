mod = 998244353

D = dict()
def solve(x,mod):
    if x in D:
        return D[x]
    else:
        x0 = x//2
        x1 = x//2
        if x % 2 != 0:
            x1 += 1
        if x < x0*x1:
            D[x] = solve(x0,mod) * solve(x1,mod) % mod
            return D[x]
        else:
            D[x] = x % mod
            return D[x]

def main():
    x = int(input())
    print(solve(x,mod))

if __name__ == "__main__":
    main()
