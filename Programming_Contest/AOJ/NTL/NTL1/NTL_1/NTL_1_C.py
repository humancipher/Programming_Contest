import fractions

n = int(input())
Numbers =list(map(int,input().split()))

def lcm(Numbers):
    N = len(Numbers)
    if N == 1:
        return Numbers[0]
    else:
        Numbers[N-2] = \
        Numbers[N-1]*Numbers[N-2] \
        //fractions.gcd(Numbers[N-1],Numbers[N-2])
        return lcm(Numbers[0:N-1])

print(lcm(Numbers))
