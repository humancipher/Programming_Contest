S = [input() for _ in range(3)]

C = [[0]*26 for _ in range(3)]
for i in range(3):
    for j in range(len(S[i])):
        C[i][ord(S[i][j])-ord("A")] += 1

ans = "YES"
for j in range(26):
    if C[0][j]+C[1][j] < C[2][j]:
        ans = "NO"
        break
if ans == "YES":
    x0,x1 = 0,0
    for j in range(26):
        x0 += min(C[0][j],C[2][j])
        x1 += min(C[1][j],C[2][j])
    if min(x0,x1) < len(S[0])//2: #出せるだけ出す前提で半分出せないならアウト
        ans = "NO"
print(ans)
