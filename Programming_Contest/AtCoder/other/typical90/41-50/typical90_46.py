n = int(input())
A = list(map(int,input().split()))
B = list(map(int,input().split()))
C = list(map(int,input().split()))
DA,DB,DC = dict(),dict(),dict()
for i in range(n):
    if A[i] % 46 not in DA:
        DA[A[i] % 46] = 1
    else:
        DA[A[i] % 46] += 1
    if B[i] % 46 not in DB:
        DB[B[i] % 46] = 1
    else:
        DB[B[i] % 46] += 1
    if C[i] % 46 not in DC:
        DC[C[i] % 46] = 1
    else:
        DC[C[i] % 46] += 1

ans = 0
for x in DA:
    for y in DB:
        for z in DC:
            if (x+y+z) % 46 == 0:
                ans += DA[x] * DB[y] * DC[z]
print(ans)