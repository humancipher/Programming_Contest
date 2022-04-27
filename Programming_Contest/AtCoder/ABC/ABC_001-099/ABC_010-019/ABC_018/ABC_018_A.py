L = list()
for i in range(3):
    a = int(input())
    L.append([a,i])
L.sort(key = lambda x:x[0],reverse=True)
Ans = [None for _ in range(3)]
for i in range(3):
    a,b = L[i]
    Ans[b] = i+1
for i in range(3):
    print(Ans[i])
