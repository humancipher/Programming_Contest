from copy import copy

def shortcut(C):
    COM = ["A","B","X","Y"]
    COM2 = []
    for a in COM:
        for b in COM:
            COM2.append(a+b)

    output = len(C)
    for s in COM2:
        for t in COM2:
            if s != t:
                B = copy(C)
                pt = 0
                while pt < len(B)-1:
                    if B[pt]+B[pt+1] == s or B[pt]+B[pt+1] == t:
                        B = B[:pt] + "S" + B[pt+2:]
                    pt += 1
                output = min(output,len(B))
    return output

N = int(input())
c = input()

print(shortcut(c))
