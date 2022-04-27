N = int(input())
A = list(map(int,input().split()))

for i in range(1,N):
    A[i] += A[i-1]

diff_min = 10**16

for i in range(N):
    diff_min = min(diff_min,abs(A[N-1]-2*A[i]))

print(diff_min)
