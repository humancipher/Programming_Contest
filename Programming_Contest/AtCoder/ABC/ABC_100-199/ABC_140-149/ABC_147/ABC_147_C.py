N = int(input())
S = []
for _ in range(N):
    a = int(input())
    S_ = []
    for _ in range(a):
        S_.append(tuple(map(int,input().split())))
    S.append(S_)

def judge(S,bin):
    #矛盾があるかどうかの判定
    #正直者:1,不親切な人:0
    for i in range(N):
        if bin[i] == 1:
            for j in range(len(S[i])):
                if (S[i][j][1] == 1 and bin[S[i][j][0]-1] != 1) \
                or (S[i][j][1] == 0 and bin[S[i][j][0]-1] != 0):
                    return False
    return True

ans = 0
for i in range(2**N):
    b = bin(i)
    b = b[2:]
    while len(b) < N:
        b = "0"+b
    bit = []
    for j in range(len(b)):
        if b[j] == "0":
            bit.append(0)
        else:
            bit.append(1)
    if judge(S,bit):
        ans = max(ans,sum(bit))

print(ans)
