from bisect import bisect_right

#半分全列挙
def half_rekkyo(VW,n,w):
    HF = VW[:n//2]
    HF2 = VW[n//2:]
    D1,D2 = dict(),dict()
    DL1,DL2 = list(),list()
    DLB2 = list()
    for i in range(2**(len(HF))):
        a,b = 0,0
        for j in range(len(HF)):
            if 2**j & i:
                a += HF[j][0]
                b += HF[j][1]
        if b <= w:
            if b in D1:
                D1[b] = max(D1[b],a)
            else:
                D1[b] = a
    for i in range(2**(len(HF2))):
        a,b = 0,0
        for j in range(len(HF2)):
            if 2**j & i:
                a += HF2[j][0]
                b += HF2[j][1]
        if b <= w:
            if b in D2:
                D2[b] = max(D2[b],a)
            else:
                D2[b] = a
    for x in D1:
        DL1.append([x,D1[x]])
    for x in D2:
        DL2.append([x,D2[x]])
        DLB2.append(x)
    DL1.sort(key = lambda x:x[0])
    DL2.sort(key = lambda x:x[0])
    DLB2.sort()
    for i in range(len(DL1)-1):
        DL1[i+1][1] = max(DL1[i+1][1],DL1[i][1])
    for i in range(len(DL2)-1):
        DL2[i+1][1] = max(DL2[i+1][1],DL2[i][1])
    ans = 0
    for i in range(len(DL1)):
        bs = bisect_right(DLB2,w-DL1[i][0])
        tmp = DL1[i][1] + DL2[bs-1][1]
        ans = max(ans,tmp)
    return ans