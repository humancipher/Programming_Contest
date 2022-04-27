h,w,a,b = map(int,input().split())

L = []
for i in range(h):
    if i < b:
        tmp = "0" * a + "1" * (w-a)
    else:
        tmp = "1" * a + "0" * (w-a)
    L.append(tmp)
for i in range(h):
    print(L[i])
