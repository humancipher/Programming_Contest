N,X = map(int,input().split())

M = [int(input()) for _ in range(N)]

ans,X = N,X - sum(M)

m = min(M)

ans += X // m

print(ans)
