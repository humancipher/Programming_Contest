from math import sqrt

def Tri(n):
    #三角数:自然数aを用いてa(a+1)//2で表現できる数
    n *= 2
    sq_n = int(sqrt(n))
    if sq_n * (sq_n+1) == n:
        return True
    else:
        return False

def Pent(n):
    #五角数：自然数aを用いてa(3a-1)//2で表現できる数
    #x(3x-1)//2=nの正の解はx=(1+sqrt(1+24n))/6
    #解の公式を使えばO(1)で判定できた...
    x = int((1+int(sqrt(1+24*n)))//6)
    #誤差が発生しにくいようになるべく整数型で扱う
    if x*(3*x-1)//2 == n:
        return True
    else:
        return False

def main():
    n = 144
    n_lim = 10**5

    while n < n_lim:
        hexa = n*(2*n-1)
        if Tri(hexa) and Pent(hexa):
            break
        else:
            n += 1

    if n < n_lim:
        print(hexa)
    else:
        print("over")

if __name__ == "__main__":
    main()
