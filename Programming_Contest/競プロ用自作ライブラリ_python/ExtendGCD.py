def extgcd(a, b): # 出力:(gcd(a,b),x,y) a*x + b*y = gcd(a,b)を満たすx,y
    if b:
        d, y, x = extgcd(b, a % b)
        y -= (a // b)*x
        return d, x, y
    return a, 1, 0