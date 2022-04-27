def main():
    n = int(input())

    C = [25,10,5,1]
    ans = 0
    for i in range(4):
        ans += n // C[i]
        n %= C[i]

    print(ans)

if __name__ == "__main__":
    main()
