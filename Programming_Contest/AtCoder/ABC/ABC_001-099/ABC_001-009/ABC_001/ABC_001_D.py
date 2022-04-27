def format(x):
    if len(str(x)) == 4:
        return str(x)
    else:
        return "0"*(4-len(str(x))) + str(x)

n = int(input())
SE = []
for _ in range(n):
    s,e = map(int,input().split("-"))
    s -= s % 5
    if e % 5 != 0:
        e += 5 - (e % 5)
    if e % 100 == 60:
        e += 40
    SE.append([s,e])

M = [0] * 2402
for s,e in SE:
    M[s] += 1
    M[e+1] -= 1
for i in range(1,2402):
    M[i] += M[i-1]
Ans = []
pt = 0
while pt < 2402:
    if M[pt] > 0:
        left = pt
        while M[pt] > 0:
            pt += 1
        right = pt-1
        Ans.append([format(left),format(right)])
    pt += 1
for i in range(len(Ans)):
    print(Ans[i][0] + "-" + Ans[i][1])
