S = input()

if len(S) % 2 != 0:
    print("No")
else:
    i,flag = 0,True
    while i+1 <= len(S):
        if S[i] == "h" and S[i+1] == "i":
            i += 2
        else:
            flag = False
            break
    if flag:
        print("Yes")
    else:
        print("No")
