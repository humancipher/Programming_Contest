def solve(P,n):
    P = [0] + P
    Ans = []
    R = [None] *(n+1)
    for i in range(n+1):
        R[P[i]] = i
    cnt,now = 0,0
    while cnt < n and now < n:
        while R[now] > now and cnt < n:
            cnt += 1
            rn = R[now]
            Ans.append(rn-1)
            R[now] -= 1
            R[P[rn-1]] += 1
            P[rn],P[rn-1] = P[rn-1],P[rn]
        now += 1
    flag = (cnt == n-1)
    if flag:
        for i in range(n+1):
            if P[i] != R[i]:
                flag = False
                break
    if flag and len(set(Ans)) == n-1:
        return Ans
    else:
        return [-1]

n = int(input())
P = list(map(int,input().split()))
ans = solve(P,n)
for i in range(len(ans)):
    print(ans[i])
