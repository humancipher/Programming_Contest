S = list(input())

if 97 <= ord(S[0]) <= 122:
    S[0] = chr(ord(S[0])-32)

for i in range(1,len(S)):
    if 65 <= ord(S[i]) <= 90:
        S[i] = chr(ord(S[i])+32)

S = "".join(S)
print(S)
