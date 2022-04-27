S = input()
S = "." + S + "#"
cnt = 0
Ans = []
for i in range(1,len(S)):
    if S[i] == S[i-1]:
        cnt += 1
    else:
        Ans.append(S[i-1])
        Ans.append(str(cnt))
        cnt = 1
print("".join(Ans[2:]))