N = 1000
F = [0,1,1]
pt = 2
while len(str(F[pt])) < N:
    F.append(F[pt]+F[pt-1])
    pt += 1

print(pt)
