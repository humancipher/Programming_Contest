n = int(input())
S = list(input())
T = list()
for i in range(n):
    if S[i] == "A":
        T.append("B")
        T.append("B")
    else:
        T.append(S[i])
T.append("D")
U = list()
pt = 0
while pt < len(T)-1:
    if T[pt] == "B" and T[pt+1] == "B":
        U.append("A")
        pt += 2
    else:
        U.append(T[pt])
        pt += 1
print("".join(U))