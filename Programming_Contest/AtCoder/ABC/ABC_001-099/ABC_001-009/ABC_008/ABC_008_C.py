n = int(input())
C = [int(input()) for _ in range(n)]

D = [-1] * n #D[i]:C[i] % C[j] == 0 を満たすj!=iの数
for i in range(n):
    for j in range(n):
        if C[i] % C[j] == 0:
            D[i] += 1

ans = 0
for i in range(n):
    if D[i] % 2 != 0:
        ans += 1 / 2
    else:
        ans += (D[i]+2) / (2*D[i]+2)
print(ans)