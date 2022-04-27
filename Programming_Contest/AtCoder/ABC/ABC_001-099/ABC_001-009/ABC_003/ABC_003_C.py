def main():
    N,K = map(int,input().split())
    R = list(map(int,input().split()))

    R.sort(reverse = True)

    ans = 0
    for i in reversed(range(K)):
        ans = (ans + R[i])/2

    print(ans)

if __name__ == "__main__":
    main()
