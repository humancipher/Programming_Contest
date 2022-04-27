S = input()
gcnt,pcnt = 0,0
ans = 0
for i in range(len(S)):
    if S[i] == "g" and pcnt < gcnt:
        pcnt += 1
        ans += 1
    elif S[i] == "g" and pcnt >= gcnt:
        gcnt += 1
    elif S[i] == "p" and pcnt < gcnt:
        pcnt += 1
    elif S[i] == "p" and pcnt >= gcnt:
        gcnt += 1
        ans -= 1
print(ans)