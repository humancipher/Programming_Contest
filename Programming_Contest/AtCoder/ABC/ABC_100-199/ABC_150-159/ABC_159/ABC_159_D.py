import collections

N = int(input())
A = list(map(int,input().split()))
AS = set(A)

def comb(n):
    return n*(n-1)//2

L = collections.Counter(A)

ans_tmp = 0
for a in AS:
    ans_tmp += comb(L[a])

for i in range(N):
    ans = ans_tmp
    ans += (comb(L[A[i]]-1) - comb(L[A[i]]))

    print(ans)
