a,b,c = map(int,input().split())
a %= 10
if a == 0:
    ans = 0
else:
    a0 = a
    S = [a0]
    a *= a0
    a %= 10
    while a != a0:
        S.append(a)
        a *= a0
        a %= 10
    shuki = len(S)
    S = [None] + S
    bc = pow(b,c,shuki)
    if bc == 0:
        bc = shuki
    ans = pow(a0,bc,10)
print(ans)
