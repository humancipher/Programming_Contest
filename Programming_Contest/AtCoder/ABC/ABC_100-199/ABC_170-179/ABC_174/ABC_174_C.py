K = int(input())

S = set()
cnt,n = 1,7
nothing = False

while True:
    if n % K == 0:
        print(cnt)
        break
    else:
        if n in S:
            print(-1)
            break
        else:
            S.add(n)
            n += (7 * pow(10,cnt,K))
            n %= K
            cnt += 1
