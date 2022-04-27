HW = [list(map(int,input().split())) for _ in range(2)]

if HW[1][0] in HW[0] or HW[1][1] in HW[0]:
    print("YES")
else:
    print("NO")
