def solve(N):
    if N < 10**3:
        return 0
    else:
        ans = 0
        ans += max(0,N - 10**3 + 1)
        ans += max(0,N - 10**6 + 1)
        ans += max(0,N - 10**9 + 1)
        ans += max(0,N - 10**12 + 1)
        ans += max(0,N - 10**15 + 1)

        return ans

def main():
    print(solve(int(input())))

if __name__ == "__main__":
    main()

        