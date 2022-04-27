N,K = map(int,input().split())

div = N % K
ans = min(div,abs(div-K))

print(ans)
