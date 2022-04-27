N = int(input())
a = list(map(int,input().split()))

S = sum(a)
if (S // N) * N != S:
    print(-1)
else:
    tmp,pt,ans,avg = 0,0,0,S//N
    b = [0 for _ in range(N)]
    b[0] = a[0]
    for i in range(1,N):
        b[i] = b[i-1] + a[i]
    while pt < N-1:
        if b[pt] != avg*(pt+1):
            ans += 1
        pt += 1
    print(ans)
