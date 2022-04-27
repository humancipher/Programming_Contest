N = input()

cnt = 0
for i in range(len(N)):
    cnt += int(N[i])
    cnt %= 9

if cnt == 0:
    print("Yes")
else:
    print("No")
