P = list(map(int,input().split()))

A = [chr(ord("a")+i) for i in range(26)]
Ans = []
for i in range(26):
    Ans.append(A[P[i]-1])
print("".join(Ans))