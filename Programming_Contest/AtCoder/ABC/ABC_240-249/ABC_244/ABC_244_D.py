S = list(input().split())
T = list(input().split())
D1,D2 = dict(),dict()
for i in range(3):
    D1[S[i]] = i
    D2[T[i]] = i
C = ["R","G","B"]
plus,minus = 0,0
for c in C:
    if D1[c] < D2[c]:
        plus += 1
    elif D2[c] < D1[c]:
        minus += 1
if plus % 2 == 0 or minus % 2 == 0:
    print("Yes")
else:
    print("No")