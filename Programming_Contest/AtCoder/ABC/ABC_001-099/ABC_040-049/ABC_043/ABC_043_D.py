S = input()
#もしかしてアンバランスなパターンがあるとしたら長さ2又は3のパターンで必ずある
exist = False
ans = "-1 -1"
for i in range(len(S)-1):
    if S[i] == S[i+1]:
        ans = str(i+1) + " " + str(i+2)
        exist = True
        break

if not exist:
    for i in range(len(S)-2):
        if S[i] == S[i+2]:
            ans = str(i+1) + " " + str(i+3)
            exist = True
            break

print(ans)