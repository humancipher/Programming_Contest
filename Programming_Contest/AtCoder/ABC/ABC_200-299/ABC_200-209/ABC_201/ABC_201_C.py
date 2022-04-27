S = input()
V = set()
for i in range(10):
    if S[i] == "o":
        V.add(i)
cnt = 0

for i in range(10**4):
    flag,F = True,set()
    for j in range(4):
        if S[(i // 10**j) % 10] == "x":
            flag = False
        if S[(i // 10**j) % 10] == "o":
            F.add((i // 10**j) % 10)
    if flag and len(V) == len(F):
        cnt += 1
print(cnt)
