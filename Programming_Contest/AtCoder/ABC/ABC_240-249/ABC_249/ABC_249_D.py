limit = 2*10**5

n = int(input())
A = list(map(int,input().split()))

C = [0] * (limit+1)
for a in A:
    C[a] += 1
ans = 0
for i in range(1,limit+1):
    for j in range(1,limit//i+1):
        ans += C[i*j] * C[i] * C[j]
print(ans)