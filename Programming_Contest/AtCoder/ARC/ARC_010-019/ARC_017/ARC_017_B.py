n,k = map(int,input().split())
A = [int(input()) for _ in range(n)]

if k == 1:
    print(n)
else:
    B = [0]
    for i in range(n-1):
        if A[i+1]-A[i] > 0:
            B.append(1)
        else:
            B.append(0)
    for i in range(n-1):
        B[i+1] += B[i]

    ans = 0
    for i in range(n-k+1):
        if B[k+i-1]-B[i] == k-1:
            ans += 1
    print(ans)
