n = int(input())
A = list(map(int,input().split()))
B = list(map(int,input().split()))
C = list(map(int,input().split()))

DA = dict()
for i in range(n):
    if A[i] in DA:
        DA[A[i]] += 1
    else:
        DA[A[i]] = 1

DB = dict()
for i in range(n):
    if B[C[i]-1] in DB:
        DB[B[C[i]-1]] += 1
    else:
        DB[B[C[i]-1]] = 1

ans = 0
for da in DA:
    if da in DB:
        ans += DA[da] * DB[da]

print(ans)
