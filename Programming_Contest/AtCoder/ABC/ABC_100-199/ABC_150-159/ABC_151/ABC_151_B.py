N,K,M = map(int,input().split())
A = list(map(int,input().split()))

sum = 0
for i in range(len(A)):
    sum += A[i]

if N*M - sum < 0:
    print(0)
elif N*M - sum <= K:
    print(N*M - sum)
else:
    print(-1)
