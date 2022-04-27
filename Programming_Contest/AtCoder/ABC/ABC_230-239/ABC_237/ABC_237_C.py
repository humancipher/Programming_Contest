S = input()
cntL = 0
for i in reversed(range(len(S))):
    if S[i] == "a":
        cntL += 1
    else:
        break
cntR = 0
for i in range(len(S)):
    if S[i] == "a":
        cntR += 1
    else:
        break
S = "a" * max(0,cntL-cntR) + S
ans = "Yes"
for i in range(len(S)):
    if S[i] != S[len(S)-1-i]:
        ans = "No"
        break
print(ans)