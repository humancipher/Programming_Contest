def comb(n,k):
    ans = 1
    for i in range(k):
        ans *= (n-i)
    for i in range(k):
        ans //= (i+1)
    return ans

def main():
    n,a,b = map(int,input().split())
    V = list(map(int,input().split()))
    
    V.sort(reverse=True)
    avg = sum(V[:a])/a
    x = V[a-1]
    left,right = n,-1
    for i in range(n):
        if V[i] == x:
            left = min(left,i)
            right = max(right,i)
    pat = 0
    cnt = 0
    for i in range(n):
        if V[i] == x:
            cnt += 1
    if V[0] == x:
        cnt2 = a-left-1
        for i in range(a-1,b):
            if V[i] == x:
                cnt2 += 1
                pat += comb(cnt,cnt2)
    else:
        cnt2 = 0
        for i in range(a):
            if V[i] == x:
                cnt2 += 1
        pat += comb(cnt,cnt2)
    print(avg)
    print(pat)
    
if __name__ == "__main__":
    main()
