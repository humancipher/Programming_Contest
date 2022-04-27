n = int(input())
A = list(map(int,input().split()))
erase = A[0]
kakutei = False
for i in range(1,n):
    if A[i-1] > A[i]:
        kakutei = True
    if not kakutei:
        erase = max(erase,A[i])
Ans = []
for i in range(n):
    if A[i] != erase:
        Ans.append(A[i])
print(" ".join(map(str,Ans)))