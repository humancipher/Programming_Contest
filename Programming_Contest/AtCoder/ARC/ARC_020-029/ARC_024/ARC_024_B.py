n = int(input())
Col = [int(input()) for _ in range(n)]

if len(set(Col)) == 1:
    print(-1)
else:
    Col = Col + Col
    bef = Col[0]
    maxlen,tmp = 1,1
    for i in range(1,2*n):
        if Col[i] == Col[i-1]:
            tmp += 1
        else:
            maxlen = max(maxlen,tmp)
            tmp = 1
    maxlen = max(maxlen,tmp)
    print((maxlen+1)//2)