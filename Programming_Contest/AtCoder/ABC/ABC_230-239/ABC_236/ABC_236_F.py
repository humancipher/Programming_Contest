n = int(input())
C = list(map(int,input().split()))
for i in range(2**n-1):
    C[i] = [C[i],i+1]
C.sort(key = lambda x:x[0])
Used = [False] * 2**n
ans = 0
for i in range(2**n-1):
    a,b = C[i][0],C[i][1]
    if not Used[b]:
        Used[b] = True
        ans += a
        for j in range(2**n):
            if Used[j]:
                Used[j^b] = True
print(ans)