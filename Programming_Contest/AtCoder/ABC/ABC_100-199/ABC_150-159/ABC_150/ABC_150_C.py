import math
N = int(input())
P = list(map(int, input().split(" ")))
Q = list(map(int, input().split(" ")))

def DicNum(P,n): #nがPの何番目か
    count = 0
    for i in range(len(P)):
        if n < P[i]:
            count += 1
    return count

def DicNumP(P): #Pが何番目か
    count = 0
    for i in range(len(P)):
        count += DicNum(P[i:],P[i])*math.factorial(N-i-1)
    return count

print(abs(DicNumP(P)-DicNumP(Q)))
