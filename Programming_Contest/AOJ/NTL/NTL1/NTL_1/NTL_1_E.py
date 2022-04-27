a,b = map(int,input().split())

def ExtGCD(a,b): #ax+by=GCD(a,b)の解(x,y)
    flag = True
    if a < b:
        a,b = b,a
        flag = False
    r0, r1, s0, s1, t0, t1 = a, b, 1, 0, 0, 1
    while r1 != 0:
        q, r2 = r0//r1, r0%r1
        r0, s0, t0, r1, s1, t1 = r1, s1, t1, r2, s0-s1*q,t0-t1*q
    d = r0
    if flag :
        return (d,s0,t0)
    else:
        return (d,t0,s0)

print(str(ExtGCD(a,b)[1])+" "+str(ExtGCD(a,b)[2]))
