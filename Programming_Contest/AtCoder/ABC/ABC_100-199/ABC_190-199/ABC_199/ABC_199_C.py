n = int(input())
S = list(input())
q = int(input())
TAB = [map(int,input().split()) for _ in range(q)]
SL,SR = S[:n],S[n:]
S = [SL,SR]

t2 = 0 #t == 1になった回数の偶奇
for t,a,b in TAB:
    if t == 1:
        a,b = a-1,b-1
        if t2 == 0:
            a1,a2 = a // n,a % n
            b1,b2 = b // n,b % n
        else:
            a1,a2 = (a // n + 1) % 2,a % n
            b1,b2 = (b // n + 1) % 2,b % n
        S[a1][a2],S[b1][b2] = S[b1][b2],S[a1][a2]
    else:
        t2 += 1
        t2 %= 2
if t2 == 0:
    print("".join(S[0]) + "".join(S[1]))
else:
    print("".join(S[1]) + "".join(S[0]))
