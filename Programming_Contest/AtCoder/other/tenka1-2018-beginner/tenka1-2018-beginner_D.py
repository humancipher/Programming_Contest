from math import sqrt

n = int(input())

if int(sqrt(2*n)) * (int(sqrt(2*n))+1) == 2 * n: #conb(k,2) == n
    print("Yes")
    k = int(sqrt(2*n))+1
    print(k)
    S = [[] for _ in range(k+1)]
    num,pt,buf = 1,1,1
    while num <= n:
        S[pt].append(num)
        S[pt+buf].append(num)
        num += 1
        if pt+buf < k:
            buf += 1
        else:
            pt += 1
            buf = 1
    for i in range(1,k+1):
        print(k-1,end=" ")
        print(" ".join(map(str,S[i])))
else:
    print("No")
