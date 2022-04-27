def isCirc(s):
    for i in range(len(s)//2):
        if s[i] != s[len(s)-1-i]:
            return False
    return True

N = 10**6

Circ = set()
for i in range(1,N):
    if isCirc(str(i)):
        Circ.add(i)

ans = 0
for c in Circ:
    if isCirc(bin(c)[2:]):
        ans += c

print(ans)
