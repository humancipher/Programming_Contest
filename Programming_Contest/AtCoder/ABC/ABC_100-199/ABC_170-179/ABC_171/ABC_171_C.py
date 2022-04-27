def solve(N):
    ans = ""
    while N > 0:
        q,r = N // 26,N % 26
        if r == 0:
            q -= 1
            r = 26
        ans = chr(96 + r) + ans
        N = (N - r) // 26

    return ans

def main():
    N = int(input())

    print(solve(N))

if __name__ == "__main__":
    main()
