from itertools import accumulate

N = int(input())
A = list(map(int,input().split()))

sumA = sum(A)
A = list(accumulate(A))

ans = 1 << 60
for i in range(N-1):
    ans = min(ans,abs(sumA - 2 * A[i]))

print(ans)
