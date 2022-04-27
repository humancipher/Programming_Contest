n,D,H = map(int,input().split())
DH = [map(int,input().split()) for _ in range(n)]

katamuki = -10**6
for d,h in DH:
    katamuki = max(katamuki,(H-h) / (d-D))

ans = max(0,H+katamuki*D)
print(ans)
