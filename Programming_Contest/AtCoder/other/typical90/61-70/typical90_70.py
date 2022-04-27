n = int(input())
A,B = list(),list()
for _ in range(n):
    x,y = map(int,input().split())
    A.append(x)
    B.append(y)
A.sort()
B.sort()
ans = 0
for i in range(n):
    ans += abs(A[i]-A[n//2])
    ans += abs(B[i]-B[n//2])
print(ans)
