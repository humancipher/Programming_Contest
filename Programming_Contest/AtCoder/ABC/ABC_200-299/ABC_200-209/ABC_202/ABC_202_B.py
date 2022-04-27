S = list(input())
for i in range(len(S)):
    if S[i] == "6":
        S[i] = "9"
    elif S[i] == "9":
        S[i] = "6"
for i in range(len(S)//2):
    S[i],S[-1-i] = S[-1-i],S[i]
print("".join(S))
