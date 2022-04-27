N = int(input())
flag = 0
if N < 10:
    print('Yes')
    flag = 1
else:
    for i in range(2,10):
        if N % i == 0 and (N // i) < 10 and flag == 0:
                print('Yes')
                flag = 1

if flag == 0:
    print('No')
