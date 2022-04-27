def rev(N,NG):
    n = 0
    for i in range(100):
        if n + 3 not in NG and n + 3 <= N:
            n += 3
        elif n + 2 not in NG and n + 2 <= N:
            n += 2
        elif n + 1 not in NG and n + 1 <= N:
            n += 1
        else:
            return False
        if n == N:
            return True
    return False

def main():
    N = int(input())
    NG = set([int(input()) for _ in range(3)])

    if rev(N,NG):
        print("YES")
    else:
        print("NO")

if __name__ == "__main__":
    main()
