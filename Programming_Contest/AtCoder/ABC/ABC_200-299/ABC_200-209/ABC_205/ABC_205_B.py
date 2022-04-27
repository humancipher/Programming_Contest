n = int(input())
A = list(map(int,input().split()))

A.sort()
ans = "Yes"
for i in range(n):
    if A[i] != i+1:
        ans = "No"
print(ans)
