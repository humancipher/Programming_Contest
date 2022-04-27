S = input()
ans = False
for i in range(len(S)):
    if i % 2 == 0:
        if not (97 <= ord(S[i]) and ord(S[i]) <= 122):
            ans = True
    else:
        if not (65 <= ord(S[i]) and ord(S[i]) <= 90):
            ans = True
if ans:
    print("No")
else:
    print("Yes")
