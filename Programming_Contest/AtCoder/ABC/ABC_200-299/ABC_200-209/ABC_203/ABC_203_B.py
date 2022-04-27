n,k = map(int,input().split())

ans = (n*(n+1) // 2) * k * 100 + (k*(k+1) // 2) * n
print(ans)
