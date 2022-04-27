N,K = map(int,input().split())
A = list(map(int,input().split()))

A.sort()
ans = ""
if K > A[-1]:
    ans = "IMPOSSIBLE"
else:
    for i in range(N):
        if K == A[i]:
            ans = "POSSIBLE"
            break

if ans == "":
    min_diff = A[-1]
    update = True
    while update:
        update = False
        for i in range(len(A)-1):
            if 0 < A[i+1] - A[i] and A[i+1] - A[i] < min_diff:
                min_diff = A[i+1] - A[i]
                update = True
        if update:
            A.append(min_diff)
            A.sort()
    if K % A[0] == 0:
        ans = "POSSIBLE"
    else:
        ans = "IMPOSSIBLE"

print(ans)
