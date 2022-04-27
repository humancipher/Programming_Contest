S = input()

if S[0] == "A":
    flag1 = True
else:
    flag1 = False

cnt = 0
for i in range(2,len(S)-1):
    if S[i] == "C":
        cnt += 1
if cnt == 1:
    flag2 = True
else:
    flag2 = False

cnt2 = 0
for i in range(len(S)):
    if ord("a") <= ord(S[i]) and ord(S[i]) <= ord("z"):
        cnt2 += 1
if cnt2 == len(S) - 2:
    flag3 = True
else:
    flag3 = False

if flag1 and flag2 and flag3:
    print("AC")
else:
    print("WA")