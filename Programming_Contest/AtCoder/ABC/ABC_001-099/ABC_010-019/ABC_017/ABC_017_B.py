S = list(input())
update = True
while update:
    update = False
    if len(S) >= 2:
        if S[-2] == "c" and S[-1] == "h":
            S.pop()
            S.pop()
            update = True
    if len(S) >= 1:
        if S[-1] == "o" or S[-1] == "k" or S[-1] == "u":
            S.pop()
            update = True

if len(S) == 0:
    print("YES")
else:
    print("NO")