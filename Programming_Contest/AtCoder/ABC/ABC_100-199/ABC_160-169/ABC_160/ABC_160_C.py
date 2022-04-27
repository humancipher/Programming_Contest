K,N = map(int,input().split())
A = list(map(int,input().split()))

dist_max = 0
for i in range(N-1):
    dist_max = max(dist_max,A[i+1]-A[i])
dist_max = max(dist_max,K-A[N-1]+A[0])

print(K-dist_max)
