N,M = map(int,input().split())

p = 1-(1/2)**M
time = 1900 * M + 100 * (N - M)
ans = time / (1 - p)
print(int(ans))
