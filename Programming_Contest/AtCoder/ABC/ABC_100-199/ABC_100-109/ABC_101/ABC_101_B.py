N = input()

SN = 0
for i in range(len(N)):
    SN += int(N[i])

N = int(N)

if N % SN == 0:
    print("Yes")
else:
    print("No")
