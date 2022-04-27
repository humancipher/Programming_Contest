path = "./p22_input.txt"

def score(S):
    output = 0
    for i in range(len(S)):
        output += (ord(S[i]) - 64)
    return output

with open(path) as f:
    T = []
    for f_line in f:
        T += f_line.split(",")
N = len(T)
for i in range(N):
    T[i] = T[i][1:len(T[i])-1]

T.sort()

ans = 0
for i in range(N):
    ans += (i+1)*score(T[i])
print(ans)
