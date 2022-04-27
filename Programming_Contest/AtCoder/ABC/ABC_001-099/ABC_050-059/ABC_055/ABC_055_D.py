n = int(input())
S = input()

Pat = [(True,True),(True,False),(False,True),(False,False)]
Ans = [[None for _ in range(n)] for _ in range(4)] #i番目が羊かどうか

Exist = []
for p in range(4):
    Ans[p][0],Ans[p][1] = Pat[p][0],Pat[p][1]
    flag = True
    for i in range(1,n+1):
        tmp = Ans[p][(i+1)%n]
        if S[i%n] == "o":
            Ans[p][(i+1)%n] = Ans[p][i-1] ^ Ans[p][i%n] ^ True
        else:
            Ans[p][(i+1)%n] = Ans[p][i-1] ^ Ans[p][i%n]
        if tmp != Ans[p][(i+1)%n] and tmp != None:
            flag = False
    Exist.append(flag)

flag2 = True
for p in range(4):
    if Exist[p] and flag2:
        for i in range(n):
            if Ans[p][i]:
                Ans[p][i] = "S"
            else:
                Ans[p][i] = "W"
        print("".join(Ans[p]))
        flag2 = False

if flag2:
    print(-1)