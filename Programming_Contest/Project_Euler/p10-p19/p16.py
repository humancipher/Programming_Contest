N = 1000

from math import log10,ceil

digit = ceil(10**3 * log10(2))

BIGNUM = str(pow(2,N))
digit_sum = sum(map(int,BIGNUM))
print(digit_sum)
