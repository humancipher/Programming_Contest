N = int(input())
V = [int(v) for v in input().split()]

V = sorted(V)
v = V[0]
for i in range(1,len(V)):
    v = (v + V[i]) / 2
print(v)
