n,x = map(int,input().split())
S = input()
xb = bin(x)[2:]
XL = list()
for i in range(len(xb)):
    XL.append(int(xb[i]))
for i in range(n):
    if S[i] == "U":
        XL.pop()
    if S[i] == "L":
        XL.append(0)
    if S[i] == "R":
        XL.append(1)
ans = 0
for i in range(len(XL)):
    if XL[i] == 1:
        ans += 2**(len(XL)-1-i)
print(ans)