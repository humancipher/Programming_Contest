NM = list(map(int,input().split()))

NM.sort()

if NM[1] == 1:
    print(1)
elif NM[0] == 1:
    print(NM[1]-2)
else:
    print((NM[0]-2)*(NM[1]-2))
