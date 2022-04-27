S = input()
cnt = 0
C = S[0]
for i in range(1,len(S)):
    if C != S[i]:
        cnt += 1
        C = S[i]
print(cnt)
