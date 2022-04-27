def ST(A,k):
    #標準形の文字列を与えたときに
    #長さが1大きい標準形の文字列の集合を出力
    OP = []
    for a in A:
        max_cord = 0
        for i in range(len(a)):
            max_cord = max(ord(a[i]),max_cord)
        for i in range(97,max_cord+2):
            OP.append(a+chr(i))
    return OP

N = int(input())

n,A = 1,["a"]
while n < N:
    A = ST(A,n)
    n += 1

A.sort()
for i in range(len(A)):
    print(A[i])
