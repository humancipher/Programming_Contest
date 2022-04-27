def solve(N):
    a = 2
    BL = set()
    while a**2 <= N:
        tmp = a**2
        while tmp <= N:
            BL.add(tmp)
            tmp *= a
        a += 1
    return N-len(BL)

def main():
    N = int(input())
    print(solve(N))

if __name__ == "__main__":
    main()
