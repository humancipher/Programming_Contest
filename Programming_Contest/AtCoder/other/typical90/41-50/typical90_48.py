n,k = map(int,input().split())
L = list()
for _ in range(n):
    a,b = map(int,input().split())
    L.append(a-b)
    L.append(b)
L.sort(reverse=True)
print(sum(L[:k]))