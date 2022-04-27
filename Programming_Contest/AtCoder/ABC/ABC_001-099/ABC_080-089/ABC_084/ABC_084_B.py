A,B = map(int,input().split())
S = input()

ans = True
for i in range(len(S)):
    if i == A:
        if S[i] != "-":
            ans = False
    else:
        if not (48 <= ord(S[i]) <= 57):
            ans = False

if ans:
    print("Yes")
else:
    print("No")
