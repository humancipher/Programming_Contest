from itertools import permutations

S = [input() for _ in range(3)]

A = set()
for i in range(3):
    for j in range(len(S[i])):
        A.add(S[i][j])

if len(A) >= 11:
    print("UNSOLVABLE")
else:
    B = [a for a in A]
    C = [i for i in range(10)]
    P = permutations(C)
    D = dict()
    nothing = True
    for p in P:
        for i in range(len(B)):
            D[B[i]] = p[i]
        if D[S[0][0]] * D[S[1][0]] * D[S[2][0]] == 0:
            continue
        N1,N2,N3 = 0,0,0
        for j in range(len(S[0])):
            N1 += D[S[0][j]] * 10**(len(S[0])-j-1)
        for j in range(len(S[1])):
            N2 += D[S[1][j]] * 10**(len(S[1])-j-1)
        for j in range(len(S[2])):
            N3 += D[S[2][j]] * 10**(len(S[2])-j-1)
        if N1 + N2 == N3:
            print(N1)
            print(N2)
            print(N3)
            nothing = False
            break
    if nothing:
        print("UNSOLVABLE")
