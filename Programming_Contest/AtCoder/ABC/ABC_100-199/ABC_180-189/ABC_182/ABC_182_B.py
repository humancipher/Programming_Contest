N = int(input())
A = list(map(int,input().split()))

A.sort()

mx,ans = -1,-1
for k in range(2,A[-1]+1):
    tmp = 0
    for a in A:
        if a % k == 0:
            tmp += 1
    if mx < tmp:
        mx,ans = tmp,k

print(ans)
