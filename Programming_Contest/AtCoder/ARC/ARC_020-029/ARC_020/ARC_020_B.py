from typing import Reversible


n,c = map(int,input().split())
A = [int(input()) for _ in range(n)]

Even = [0] * 10
Odd = [0] * 10
for i in range(n):
    if i % 2 == 0:
        Even[A[i]-1] += 1
    else:
        Odd[A[i]-1] += 1

ans = n
for i in range(10):
    for j in range(10):
        if i != j:
            ans = min(ans,sum(Even)-Even[i]+sum(Odd)-Odd[j])
print(ans * c)
