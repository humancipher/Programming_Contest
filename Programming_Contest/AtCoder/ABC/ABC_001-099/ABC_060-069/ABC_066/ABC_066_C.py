N = int(input())
A = list(map(int,input().split()))

ans = [None for _ in range(N)]

l,r = 0,N-1
for i in range(N):
    if i % 2 == 0:
        ans[l] = A[N-1-i]
        l += 1
    else:
        ans[r] = A[N-1-i]
        r -= 1

print(" ".join(map(str,ans)))
