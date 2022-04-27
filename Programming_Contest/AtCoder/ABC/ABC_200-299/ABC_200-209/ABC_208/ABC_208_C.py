n,k = map(int,input().split())
A = list(map(int,input().split()))

B = [[A[i],i,0] for i in range(n)]
B.sort(key = lambda x:x[0])
for i in range(n):
    B[i][2] += k // n
k %= n
for i in range(k):
    B[i][2] += 1

Ans = [0] * n
for i in range(n):
    Ans[B[i][1]] += B[i][2]
for i in range(n):
    print(Ans[i])