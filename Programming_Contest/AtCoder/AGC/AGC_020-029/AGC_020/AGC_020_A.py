def main():
    from sys import stdin
    input = stdin.readline
    n,a,b = map(int,input().split())
    if (a-b) % 2 == 0:
        print("Alice")
    else:
        print("Borys")

if __name__ == "__main__":
    main()
