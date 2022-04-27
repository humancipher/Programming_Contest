def enc(s,E,Al):
    for i in range(len(s)):
        s[i] = Al[E[ord(s[i])-ord("a")]]
    return s

def dec(s,D,Al):
    for i in range(len(s)):
        s[i] = Al[D[ord(s[i])-ord("a")]]
    return s

X = input()
n = int(input())
S = [list(input()) for _ in range(n)]

Al = [chr(ord("a")+i) for i in range(26)]
E,D = dict(),dict()
for i in range(26):
    for j in range(26):
        if X[i] == Al[j]:
            D[i] = j
            E[j] = i

T = []
for i in range(n):
    T.append(enc(S[i],E,Al))
T.sort()
for i in range(n):
    T[i] = dec(T[i],D,Al)
    print("".join(T[i]))
