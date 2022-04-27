N = int(input())
A = list(map(int,input().split()))

max_h,ans = A[0],0
for i in range(1,N):
    if max_h > A[i]:
        ans += (max_h - A[i])
    else:
        max_h = A[i]

print(ans)
