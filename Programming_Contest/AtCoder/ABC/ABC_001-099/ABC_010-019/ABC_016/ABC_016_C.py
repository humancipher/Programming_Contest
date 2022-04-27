def FoF(AB,m):
    F_m = set()
    F_of_F_m = set()
    for a,b in AB:
        if a == m:
            F_m.add(b)
        if b == m:
            F_m.add(a)
    for f in F_m:
        for a,b in AB:
            if f == a and b != m:
                F_of_F_m.add(b)
            if f == b and a != m:
                F_of_F_m.add(a)
    return len(F_of_F_m - F_m)

N,M = map(int,input().split())
AB = [list(map(int,input().split())) for _ in range(M)]

for i in range(N):
    print(FoF(AB,i+1))
