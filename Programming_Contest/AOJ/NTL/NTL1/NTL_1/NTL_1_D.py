import math

n = int(input())

#Euler関数の性質
#1:pが素数のときEuler(p**k)=p**k-p**(k-1)
#2:gcd(m,n)=1のときEuler(mn)=Euler(m)*Euler(n)
def Euler(n):
    if n == 1 or n == 2:
        return 1
    else:
        a,b = 1,0
        for i in range(2,int(math.sqrt(n))+1):
            if n % i == 0:
                a = i #このときaが常に素数
                while n % a == 0:
                    n //= a
                    b += 1
                break
        if a == 1: #このときはnが素数
            return n-1
        else:
            return (a**b-a**(b-1))*Euler(n)

print(Euler(n))
