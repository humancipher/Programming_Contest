from math import sqrt,ceil

def cal_main(S):
    #xa*yb-xb*ya=Sを満たす(xa,ya),(xb,yb)を知りたい
    #L = ceil(sqrt(S))とすると
    #xa*yb-xb*ya=L**2-(L**2-S) (L**2-S >= 0)
    #これはxb*ya=L**2-S<4*L-1の計算で代用できる

    L = ceil(sqrt(S))
    for l in range(L,10**9+1):
        #forといっても実際に繰り返されるのは数回だろうが
        xb_ya = cal_sub(l**2-S)
        xb,ya = xb_ya[0],xb_ya[1]
        if 0 <= xb <= 10**9 and 0 <= ya <= 10**9:
            return [l,ya,xb,l,0,0]

def cal_sub(T):
    if T == 0:
        return [0,0]
    else:
        L = int(sqrt(T))
        for l in reversed(range(1,L+1)):
            if T % l == 0:
                return [l,T//l]

def main():
    S = int(input())

    ans = cal_main(S)
    print(" ".join(map(str,ans)))

if __name__ == "__main__":
    main()
