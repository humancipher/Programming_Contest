def g1(x):
    x = list(str(x))
    x.sort(reverse = True)
    x = "".join(x)
    return int(x)

def g2(x):
    x = list(str(x))
    x.sort()
    x = "".join(x)
    return int(x)

def f(x):
    return g1(x) - g2(x)

def solve(x,rec):
    while rec > 0:
        x = f(x)
        rec -= 1
    return x

def main():
    N,K = map(int,input().split())
    print(solve(N,K))

if __name__ == "__main__":
    main()
