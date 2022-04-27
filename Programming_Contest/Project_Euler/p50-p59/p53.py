def comb_count(n,limit):
    #nを固定したときにComb(n,r) > limitになるrの個数
    if limit == 1:
        return n+1
    else:
        r_limit = n//2
        comb,r = 1,1
        while r <= r_limit:
            comb *= (n-r+1)
            comb //= r
            if comb > limit:
                break
            else:
                r += 1
        output = 2 * (r_limit-r+1)
        if n % 2 == 0 and output > 0:
            output -= 1
        return output

def main():
    #Comb(n,r)はrがn/2に近いほど大きくなる
    limit = 10**6
    N,ans = 100,0
    for i in range(23,N+1):
        ans += comb_count(i,limit)

    print(ans)

if __name__ == "__main__":
    main()
