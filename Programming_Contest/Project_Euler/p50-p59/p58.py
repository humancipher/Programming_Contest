#pypyじゃないと遅い
from math import sqrt

def isPrime(n):
    if n == 1:
        return False
    else:
        for i in range(2,int(sqrt(n))+1):
            if n % i == 0:
                return False
        return True

def spiral_prime():
    prime_cnt,cnt = 0,1
    for r in range(2,10**5):
        R = 2*r-1
        for i in range(1,4):
            #R**2は明らかに素数ではない
            if isPrime(R**2-i*(R-1)):
                prime_cnt += 1
        cnt += 4
        if prime_cnt * 10 < cnt:
            return R
    return "limit_over"

def main():
    print(spiral_prime())

if __name__ == "__main__":
    main()
