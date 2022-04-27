N = int(input())
SP = [list(input().split()) for i in range(N)]

for i in range(N):
    SP[i][1] = int(SP[i][1])
    SP[i].append(i+1)

for i in range(N):
    for j in reversed(range(i+1,N)):
        if SP[i][0] > SP[j][0]:
            SP[i],SP[j] = SP[j],SP[i]
        elif SP[i][0] == SP[j][0] and SP[i][1] < SP[j][1]:
            SP[i],SP[j] = SP[j],SP[i]

for i in range(N):
    print(SP[i][2])
