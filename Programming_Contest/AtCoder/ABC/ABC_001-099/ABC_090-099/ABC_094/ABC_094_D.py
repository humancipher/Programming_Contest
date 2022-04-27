n = int(input())
a = list(map(int,input().split()))

a.sort()

N,K = a[n-1],a[0]

for i in range(1,n):
    if abs((N+1)//2 - K) > abs((N+1)//2 - a[i]):
        K = a[i]

print(N,K)
