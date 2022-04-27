n = int(input())
A = list(map(int,input().split()))
A.sort()

C = dict()
for a in A:
    if a in C:
        C[a] += 1
    else:
        C[a] = 1

ans = 0
for c in C:
    ans += C[c] * (n - C[c])
ans //= 2
print(ans)
