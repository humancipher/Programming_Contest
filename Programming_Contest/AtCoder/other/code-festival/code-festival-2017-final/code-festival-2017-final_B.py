from collections import Counter

S = input()
n = len(S)
C = Counter(S)
d = (n-1)//3+1 #各文字の許容出現数
ans = "YES"
for c in C:
    if C[c] > d:
        ans = "NO"
        break
print(ans)