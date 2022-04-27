def solve(N):
    ans = 0
    for i in range(1,10**6+1):
        if int(str(i)+str(i)) <= N:
            ans += 1
        else:
            break
    return ans

def  main():
    N = int(input())
    print(solve(N))

if __name__ == "__main__":
    main()
