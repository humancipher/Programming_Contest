S = input()
Num,Cal = [0],[]
for i in range(len(S)):
    if S[i] == "*":
        Cal.append("+")
    elif S[i] == "+":
        Cal.append("*")
    else:
        if i == 0:
            Num[0] = int(S[i])
        else:
            if S[i-1] == "*" or S[i-1] == "+":
                Num.append(int(S[i]))
            else:
                Num[-1] = Num[-1] * 10 + int(S[i])
ans = Num[0]
for i in range(len(Cal)):
    if Cal[i] == "+":
        ans += Num[i+1]
    else:
        ans *= Num[i+1]
print(ans)
