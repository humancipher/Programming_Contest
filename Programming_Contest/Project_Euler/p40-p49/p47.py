from math import sqrt

def factor(n):
    F = set()
    for i in range(2,int(sqrt(n))+1):
        if n % i == 0:
            F.add(i)
            while n % i == 0:
                n //= i
        if n == 1:
            break

    if n != 1:
        return len(F)+1
    else:
        return len(F)

def main():
    #連続する4つの数で素因数がそれぞれ4種類になるような最初の数を求めたい
    n = 10**5
    n_lim = n**6
    ans = 0
    for i in range(n,n_lim):
        if factor(i) == 4:
            if factor(i+1) == 4 \
            and factor(i+2) == 4 \
            and factor(i+3) == 4:
                ans = i
                break

    if ans == 0:
        print("limit over")
    else:
        print(ans)

if __name__ == "__main__":
    main()
