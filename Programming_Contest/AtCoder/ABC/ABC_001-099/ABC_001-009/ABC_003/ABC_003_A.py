N = int(input())

if N % 2 == 0:
    print((N//2)*10**4+5*10**3)
else:
    print((N//2+1)*10**4)
