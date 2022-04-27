S = input()

not_int = False
for i in range(len(S)):
    if 97 <= ord(S[i]) and ord(S[i]) <= 122:
        not_int = True
        break

if not_int:
    print("error")
else:
    S = int(S)
    print(2*S)
