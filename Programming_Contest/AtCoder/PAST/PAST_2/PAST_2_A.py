S = list(input().split())

for i in range(2):
    if S[i][0] == "B":
        S[i] = -int(S[i][1])
    else:
        S[i] = int(S[i][0])

if S[0] > S[1]:
    S[0],S[1] = S[1],S[0]

if S[0] < 0 and S[1] > 0:
    print(S[1]-S[0]-1)
else:
    print(S[1]-S[0])
