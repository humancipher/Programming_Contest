W = set()
n = int(input())
for _ in range(n):
    a = int(input())
    if a in W:
        W.discard(a)
    else:
        W.add(a)
print(len(W))