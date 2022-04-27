from bisect import bisect_left

n = int(input())
A = [int(input()) for _ in range(n)]

E = [-A[0]]
#条件を満たすように並べたときの末尾のリスト
#降順に並べつつbisect_leftを使いたいので符号を逆にした

for i in range(1,n):
    if A[i] <= -E[-1]:
        E.append(-A[i])
    else:
        pt = bisect_left(E,-A[i]+1)
        E[pt] = -A[i]
print(len(E))
