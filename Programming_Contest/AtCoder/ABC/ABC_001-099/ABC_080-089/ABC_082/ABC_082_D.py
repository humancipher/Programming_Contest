S = input()
n = len(S)
x,y = map(int,input().split())

sw = True #x軸向き
st = True #1度も向きが変わっていない
dpx = [False] * (2*n+1) #dpx[i]:x座標がi+nのパターンがあるかどうか
dpy = [False] * (2*n+1) #dpy[i]:y座標がi+nのパターンがあるかどうか
dpx[n],dpy[n] = True,True
dist = 0
for i in range(n):
    if S[i] == "T":
        if sw:
            ndpx = [False] * (2*n+1)
            for j in range(2*n+1):
                if j+dist < 2*n+1:
                    ndpx[j+dist] |= dpx[j]
                if j-dist >= 0 and not st:
                    ndpx[j-dist] |= dpx[j]
            dpx = ndpx
        else:
            ndpy = [False] * (2*n+1)
            for j in range(2*n+1):
                if j+dist < 2*n+1:
                    ndpy[j+dist] |= dpy[j]
                if j-dist >= 0:
                    ndpy[j-dist] |= dpy[j]
            dpy = ndpy
        sw ^= True
        st = False
        dist = 0
    else:
        dist += 1

if S[n-1] == "F":
    if sw:
        ndpx = [False] * (2*n+1)
        for j in range(2*n+1):
            if j+dist < 2*n+1:
                ndpx[j+dist] |= dpx[j]
            if j-dist >= 0 and not st:
                ndpx[j-dist] |= dpx[j]
        dpx = ndpx
    else:
        ndpy = [False] * (2*n+1)
        for j in range(2*n+1):
            if j+dist < 2*n+1:
                ndpy[j+dist] |= dpy[j]
            if j-dist >= 0:
                ndpy[j-dist] |= dpy[j]
        dpy = ndpy
if dpx[n+x] and dpy[n+y]:
    print("Yes")
else:
    print("No")