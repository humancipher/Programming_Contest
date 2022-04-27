A,B = map(int,input().split())
if A > B:
    A,B = B,A

def no_tax(tax,tax_r):
    origin,min,max = 0,0,0
    while int(origin*tax_r) < tax:
        origin += 1
    min = origin
    while int(origin*tax_r) <= tax:
        origin += 1
    max = origin-1
    return (min,max)

A_min,A_max,B_min,B_max = \
no_tax(A,0.08)[0],no_tax(A,0.08)[1],no_tax(B,0.1)[0],no_tax(B,0.1)[1]

if A_min <= B_max and B_min <= A_max:
    print(max(A_min,B_min))
else:
    print(-1)
