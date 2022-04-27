n = int(input())
t = input()
V = [(1,0),(0,-1),(-1,0),(0,1)]
now = 0
x,y = 0,0
for i in range(n):
    if t[i] == "S":
        x += V[now][0]
        y += V[now][1]
    else:
        now += 1
        now %= 4
print(x,y)