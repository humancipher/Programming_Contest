from math import sqrt
from copy import copy

def eratos(n_min,n_max):
    #n_min以上n_max以下の素数のリストを作成
    L = [True for _ in range(n_max+1)]
    L[0],L[1] = False,False

    for i in range(2,int(sqrt(n_max))+1):
        if L[i]:
            for j in range(2,n_max//i+1):
                L[i*j] = False

    P = list()
    for i in range(n_min,n_max+1):
        if L[i]:
            P.append(i)

    return P

def perm(P_abc):
    for i in range(len(P_abc)):
        P_abc[i] = list(str(P_abc[i]))
        P_abc[i].sort()
        P_abc[i] = "".join(P_abc[i])

    S = set()
    for i in range(len(P_abc)):
        S.add(P_abc[i])

    if len(S) == 1:
        return True
    else:
        return False

def main():
    P = eratos(10**3,10**4)
    P_set = set(P)
    ans_list = []
    c = 0
    for i in range(len(P)-2):
        for j in range(i+2,len(P)):
            if (P[i]+P[j])//2 in P_set:
                P_abc = [P[i], (P[i]+P[j])//2, P[j]]
                if perm(P_abc.copy()):
                    ans_list.append(P_abc)

    print(ans_list)

if __name__ == "__main__":
    main()
