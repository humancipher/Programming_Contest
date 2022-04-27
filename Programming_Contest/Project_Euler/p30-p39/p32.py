def pand(a,b,c,N):
    a,b,c = str(a),str(b),str(c)
    abc = a+b+c
    if len(abc) != N:
        return False
    L = [False for _ in range(N)]
    #L[i]:数字i+1が1回登場した
    for i in range(len(abc)):
        if int(abc[i]) == 0:
            return False
        elif L[int(abc[i])-1] == False:
            L[int(abc[i])-1] = True
        else:
            return False
    return True

N = 9

#a*b=cでa,b,cを繋げたものが1~9のパンデジタルになるとしたら
#(len(a),len(b),len(c)) = (1,4,4),(2,3,4)のみ

Pro_set = set()
for a in range(1,10):
    for b in range(1234,9877):
        c = a*b
        if len(str(c)) == 4:
            if pand(a,b,c,N) and c not in Pro_set:
                Pro_set.add(c)

for a in range(12,99):
    for b in range(123,988):
        c = a*b
        if len(str(c)) == 4:
            if pand(a,b,c,N) and c not in Pro_set:
                Pro_set.add(c)

print(sum(Pro_set))
