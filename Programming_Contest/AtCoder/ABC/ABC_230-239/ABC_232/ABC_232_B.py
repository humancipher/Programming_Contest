S = input()
T = input()

S0 = [ord(S[i])-ord("a") for i in range(len(S))]
T0 = [ord(T[i])-ord("a") for i in range(len(T))]

ans = "No"
for k in range(26):
    flag = True
    for i in range(len(S)):
        if (S0[i]+k) % 26 != T0[i]:
            flag = False
            break
    if flag:
        ans = "Yes"
        break
print(ans)