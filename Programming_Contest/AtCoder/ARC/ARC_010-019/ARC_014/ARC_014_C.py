n = int(input())
C = [0,0,0]
S = input()
for i in range(n):
    if S[i] == "R":
        C[0] += 1
        C[0] %= 2
    if S[i] == "G":
        C[1] += 1
        C[1] %= 2
    if S[i] == "B":
        C[2] += 1
        C[2] %= 2
print(sum(C))