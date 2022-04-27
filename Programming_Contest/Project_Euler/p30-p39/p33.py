from math import gcd

def judge(a,b):
    a,b,C = str(a),str(b),[]
    if a[1] == "0" and b[1] == "0":
        return False
    if a[0] == b[0] and b[1] != "0":
        C.append((int(a[1]),int(b[1])))
    if a[0] == b[1] and b[0] != "0":
        C.append((int(a[1]),int(b[0])))
    if a[1] == b[0] and b[1] != "0":
        C.append((int(a[0]),int(b[1])))
    if a[1] == b[1] and b[0] != "0":
        C.append((int(a[0]),int(b[0])))
    a,b = int(a),int(b)
    for a_,b_ in C:
        if a*b_ == b*a_:
            return True
    return False

nume,deno = 1,1
for a in range(10,99):
    for b in range(a+1,100):
        if judge(a,b):
            nume *= a
            deno *= b
g = gcd(nume,deno)
print(deno//g)
