def main():
    m = 10**10

    ans = 0
    for i in range(1,1001):
        if i % 10 != 0:
            ans += pow(i,i,m)
            ans %= m

    print(ans)

if __name__ == "__main__":
    main()
