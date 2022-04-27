def comb(n,k,mod):
    bunsi,bunbo = 1,1
    for i in range(k):
        bunsi *= n-i
        bunsi %= mod
        bunbo *= pow(i+1,mod-2,mod)
        bunbo %= mod
    ans = (bunsi * bunbo) % mod
    return ans

#重複組合せ
def dupcomb(n,k,mod):
    return comb(n+k-1,k,mod)