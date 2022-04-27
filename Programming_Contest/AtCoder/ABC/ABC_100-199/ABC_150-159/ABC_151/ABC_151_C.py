#WAの原因：WAを数えるのはACを出したやつだけ. 問題を丁寧に読もう

N,M = map(int,input().split())
PS = []
for i in range(M):
    PS.append(input().split())
    PS[i][0] = int(PS[i][0])

WA = [0 for i in range(N+1)]
AC = [0 for i in range(N+1)]

for i in range(M):
    if PS[i][1] == "WA":
        if AC[PS[i][0]] == 0:
            WA[PS[i][0]] += 1
    else:
        AC[PS[i][0]] = 1

pen,cor = 0,0
for i in range(N+1):
    if AC[i] == 1:
        pen += WA[i]
    cor += AC[i]

print(str(cor)+" "+str(pen))
