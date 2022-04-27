A = input()
n = len(A)

allpat = n*25
pali = 0
cnt = 0
for i in range(n//2):
    if A[i] != A[n-1-i]:
        cnt += 1
if n % 2 == 0:
    if cnt == 1:
        pali = 2
else:
    if cnt == 1:
        pali = 2
    if cnt == 0:
        pali = 25

print(allpat-pali)
