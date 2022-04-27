N = int(input())
a = list(map(int,input().split()))
a = [None] + a

b = [None for _ in range(N+1)]

for i in range(N//2+1,N+1):
    b[i] = a[i]

possible = True
for i in reversed(range(1,N//2+1)):
    s = 0
    for j in range(2,int(N/i)+1):
        s = (s+b[i*j]) % 2
    if b[i] == None:
        b[i] = (a[i] + s) % 2
    elif b[i] != (a[i] + s) % 2:
        possible = False
        break

if possible:
    Ans = []
    for i in range(1,N+1):
        if b[i] == 1:
            Ans.append(str(i))
    print(len(Ans))
    ans = " ".join(Ans)
    if ans != "":
        print(ans)
else:
    print(-1)
