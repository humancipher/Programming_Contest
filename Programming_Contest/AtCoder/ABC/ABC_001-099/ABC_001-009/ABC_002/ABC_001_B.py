S = list(input())

for i in range(len(S)):
    if S[i] == "a" \
    or S[i] == "i" \
    or S[i] == "u" \
    or S[i] == "e" \
    or S[i] == "o":
        S[i] = ""

S = "".join(S)
print(S)
