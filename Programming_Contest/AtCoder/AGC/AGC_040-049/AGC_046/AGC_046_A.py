def solve(X):
    cnt = 1
    while True:
        if (X * cnt) % 360 == 0:
            return cnt
        else:
            cnt += 1

def main():
    X = int(input())
    print(solve(X))

if __name__ == "__main__":
    main()
