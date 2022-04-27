n = int(input())

for a in range(1,3501):
    for b in range(1,3501):
        if 4*a*b-a*n-b*n > 0:
            if a * b * n % (4*a*b-a*n-b*n) == 0:
                c = a*b*n // (4*a*b-a*n-b*n)
                print(a,b,c)
                exit()
