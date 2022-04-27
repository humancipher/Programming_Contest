S = [input() for _ in range(2)]

if S[0][0] == S[0][1] or S[0][0] == S[1][0] or S[1][1] == S[1][0] or S[1][1] == S[0][1]:
    print("Yes")
else:
    print("No")
