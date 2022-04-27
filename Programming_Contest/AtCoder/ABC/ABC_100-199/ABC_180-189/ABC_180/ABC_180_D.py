X,Y,A,B = map(int,input().split())

kei = 0
while (A-1) * X <= B:
    if A * X < Y:
        X *= A
        kei += 1
    else:
        break

kei += (Y - 1 - X) // B
print(kei)
