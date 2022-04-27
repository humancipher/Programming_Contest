def half(VW,n,W):
    D = dict()
    D[0] = 0
    for i in range(2**n):
        a,b = 0,0
        for j in range(n):
            if 2**j & i:
                [v,w] = VW[j]
                a += v
                b += w
        if b <= W:
            if b not in D:
                D[b] = a
            else:
                D[b] = max(D[b],a)
    Tmp = [[d,D[d]] for d in D]
    Tmp.sort(key = lambda x:x[0])
    Ans = [Tmp[0]]
    pt = 1
    while pt < len(Tmp):
        if Ans[-1][1] >= Tmp[pt][1]:
            pt += 1
        else:
            Ans.append(Tmp[pt])
            pt += 1
    return Ans

def b_search(VW,n,key):
    if VW[-1][0] <= key:
        return n-1
    left,right = 0,n
    #VW[left][1] <= key < VW[right][1]
    while right -left > 1:
        mid = (left+right)//2
        if VW[mid][0] <= key:
            left = mid
        else:
            right = mid
    return left

def solve(VW,n,W):
    ans = 0
    VW_half = VW[n//2:]
    HF = half(VW_half,n//2,W)
    for i in range(n//2):
        [v,w] = VW[i]
        if w <= W:
            tmp = v + HF[b_search(HF,len(HF),W-w)][1]
            ans = max(tmp,ans)
    return ans

def main():
    n,W = map(int,input().split())
    VW = [list(map(int,input().split())) for _ in range(n)]
    ans = solve(VW,n,W)
    print(ans)

if __name__ == "__main__":
    main()
