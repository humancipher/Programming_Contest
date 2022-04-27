S = input()

cnt,c_max = 0,0
for i in range(3):
    if S[i] == "R":
        cnt += 1
        c_max = max(c_max,cnt)
    else:
        cnt = 0

print(c_max)
