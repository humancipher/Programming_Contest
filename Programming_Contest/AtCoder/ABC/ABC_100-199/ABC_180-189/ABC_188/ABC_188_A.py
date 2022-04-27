XY = list(map(int,input().split()))

XY.sort()

if XY[0] + 3 > XY[1]:
    print("Yes")
else:
    print("No")
