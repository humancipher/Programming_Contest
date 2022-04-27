S = input()
T = input()

Diff = []
for i in range(len(S)):
    if S[i] != T[i]:
        Diff.append(i)

ans = "Yes"
if len(Diff) == 2:
    if not (S[Diff[0]] == T[Diff[0]+1]) or not (S[Diff[0]+1] == T[Diff[0]]):
        ans = "No"
if len(Diff) != 2 and len(Diff) != 0:
    ans = "No"
print(ans)
