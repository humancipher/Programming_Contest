N = int(input())
S = input()

x,max_x = 0,0
for i in range(len(S)):
    if S[i] == "I":
        x += 1
        max_x = max(max_x,x)
    if S[i] == "D":
        x -= 1

print(max_x)
