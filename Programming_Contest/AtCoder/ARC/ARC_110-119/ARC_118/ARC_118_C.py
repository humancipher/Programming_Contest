n = int(input())
m = 2500
B = [6,10,15]
Kouho = []
for i in range(1,m+1):
    for j in range(len(B)):
        Kouho.append(i * B[j])
Ans,S = list(),set()
for i in range(len(Kouho)):
    if Kouho[i] <= 10000:
        if Kouho[i] not in S:
            Ans.append(Kouho[i])
            S.add(Kouho[i])
print(" ".join(map(str,Ans[:n])))