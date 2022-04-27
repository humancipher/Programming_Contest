from math import sqrt
from itertools import permutations

def isPrime(n):
    if n == 1:
        return False
    for i in range(2,int(sqrt(n))+1):
        if n % i == 0:
            return False
    return True

def main():
    #10桁以上はそもそもパンデジタル数にならない
    #9桁もパンデジタル素数にならない
    #（∵9桁のパンデジタル数だと各桁の和が45,よって3の倍数）
    #同様に8桁もあり得ない
    #あり得るとしたら7桁まで
    ans,digit = 0,7
    while ans == 0:
        A = [str(i+1) for i in range(digit)]
        B = list(permutations(A))
        for i in range(len(B)):
            B[i] = int("".join(B[i]))
        B.sort(reverse = True)

        for i in range(len(B)):
            if isPrime(B[i]):
                ans = B[i]
                break
        digit -= 1

    print(ans)

if __name__ == "__main__":
    main()
