from bisect import bisect_left

n = int(input())
A = list(map(int,input().split()))
AS = set(A)
ASL = list(AS)
ASL.sort()

BS = [[] for _ in range(len(AS))]
for i in range(n):
    bs = bisect_left(ASL,A[i])
    BS[bs].append(i)

Ans = list()
q = int(input())
for _ in range(q):
    l,r,x = map(int,input().split())
    if x in AS:
        pt = bisect_left(ASL,x)
        ans = bisect_left(BS[pt],r)-bisect_left(BS[pt],l-1)
        Ans.append(ans)
    else:
        Ans.append(0)
for i in range(q):
    print(Ans[i])