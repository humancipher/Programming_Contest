def judge(S,N):
    Ans = [False for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if S[i][j] == "o":
                Ans[j] = True
    ans = True
    for a in Ans:
        ans &= a
    return ans

def solve(S,N):
    SS = S*2
    T = []
    for i in range(N):
        t = SS[i:N+i]
        T.append(t)
    dum = "x" * N
    ans = N
    for i in range(2**N):
        U,cnt = [],0
        for j in range(N):
            if 2**j & i:
                U.append(T[j])
                cnt += 1
            else:
                U.append(dum)
        if judge(U,N):
            ans = min(ans,cnt)
    return ans

S = input()
print(solve(S,len(S)))
