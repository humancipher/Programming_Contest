def solve(A,n):
    for i in range(n):
        A[i] %= 200
    M = [[] for _ in range(200)]
    for i in range(n):
        M[A[i]].append(i)
        if len(M[A[i]]) == 2:
            return ("Yes",tuple([M[A[i]][0]]),tuple([M[A[i]][1]]))
    #この時点で答えが見つかってないなら200で割ったあまりはそれぞれ高々1個
    D = dict()
    L = []
    for i in range(200):
        if len(M[i]) == 1:
            L.append(M[i][0])
            D[M[i][0]] = i
    Pat = dict()
    for i in range(1,2**len(L)):
        tmp = 0
        tmp_L = []
        for j in range(len(L)):
            if i & 2**j:
                tmp += D[L[j]]
                tmp %= 200
                tmp_L.append(L[j])
        if tmp not in Pat:
            Pat[tmp] = tuple(tmp_L)
        else:
            return ("Yes",Pat[tmp],tuple(tmp_L))
    return ("No",(),())

n = int(input())
A = list(map(int,input().split()))
ans = solve(A, n)
print(ans[0])
if ans[0] == "Yes":
    for i in range(1,3):
        Ans = []
        for j in range(len(ans[i])):
            Ans.append(ans[i][j]+1)
        Ans.sort()
        Ans = [len(Ans)] + Ans
        print(" ".join(map(str,Ans)))
