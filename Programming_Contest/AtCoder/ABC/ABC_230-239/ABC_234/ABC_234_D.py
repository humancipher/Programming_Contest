n,k = map(int,input().split())
P = list(map(int,input().split()))

Ans = [n-k+1]
Exists = [True] * (n+1) #Exists[i]:i+1が入っている

for _ in range(n-k):
    now = P.pop()
    if now  < Ans[-1]:
        Ans.append(Ans[-1])
    else:
        pt = Ans[-1]-1
        while True:
            if Exists[pt]:
                Ans.append(pt)
                break
            else:
                pt -= 1
    Exists[now] = False

for i in reversed(range(n-k+1)):
    print(Ans[i])