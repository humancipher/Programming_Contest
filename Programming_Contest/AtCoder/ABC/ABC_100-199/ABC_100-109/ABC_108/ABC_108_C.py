def solve(N,K):
    #方針
    #a mod K == a'(a' != 0)のとき
    #b mod K == c mod K == -a'
    #(b+c) mod K == -2a'
    #これで上手くいく(-2a' mod K == 0)のはKが偶数のときのみ
    if K % 2 != 0:
        return (N // K) ** 3
    else:
        return (N // K) ** 3 + ((N + K // 2) // K) ** 3

def main():
    N,K = map(int,input().split())

    print(solve(N,K))

if __name__ == "__main__":
    main()
