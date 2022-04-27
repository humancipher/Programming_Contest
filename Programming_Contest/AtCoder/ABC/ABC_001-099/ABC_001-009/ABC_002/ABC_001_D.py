N,M = map(int,input().split())
xy = set([tuple(map(int,input().split())) for _ in range(M)])

def judge(xy,B):
    for b1 in B:
        for b2 in B:
            if b1 >= b2:
                continue
            if not (b1,b2) in xy:
                return False
    return True

ans = 0
for i in range(2**N):
    b = bin(i)
    b = b[2:]
    pad = ["0" for _ in range(N-len(b))]
    pad = "".join(pad)
    b = pad + b
    B = set([])
    for j in range(len(b)):
        if b[j] == "1":
            B.add(j+1)
    if judge(xy,B):
        ans = max(ans,len(B))

print(ans)
