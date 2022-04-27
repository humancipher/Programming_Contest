def main():
    N,C,K = map(int,input().split())
    T = [int(input()) for _ in range(N)]

    T.sort()

    ans,time,rider = 1,T[0],0
    for i in range(N):
        if T[i] <= time + K and rider < C:
            rider += 1
        else:
            ans += 1
            time = T[i]
            rider = 1

    print(ans)

if __name__ == "__main__":
    main()
