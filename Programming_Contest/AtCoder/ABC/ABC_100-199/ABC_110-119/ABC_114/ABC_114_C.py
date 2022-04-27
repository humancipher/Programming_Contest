def solve(a,N):
    if len(str(a)) >= len(str(N)):
        if a <= N and "3" in str(a) and "5" in str(a) and "7" in str(a):
            return 1
        else:
            return 0
    else:
        if "3" in str(a) and "5" in str(a) and "7" in str(a):
            return solve(10 * a + 3,N) + solve(10 * a + 5,N) + solve(10 * a + 7,N) + 1
        else:
            return solve(10 * a + 3,N) + solve(10 * a + 5,N) + solve(10 * a + 7,N)

def main():
    N = int(input())
    init_list = [3,5,7]
    ans = 0
    for a in init_list:
        ans += solve(a,N)
    print(ans)

if __name__  == "__main__":
    main()
