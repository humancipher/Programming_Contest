N = int(input())
C = list(map(int,input().split()))
Q = int(input())
S = [list(map(int,input().split())) for _ in range(Q)]
INF = 10**18+1

C_even,C_odd = [],[]
for i in range(N):
    if i % 2 == 0:
        C_odd.append(C[i])
    else:
        C_even.append(C[i])

C_odd_min = min(C_odd)
if N >= 2:
    C_even_min = min(C_even)
else:
    C_even_min = INF
#C_odd_diff:C_odd全体でのそれぞれの販売枚数
#例えばC_oddを全部1売ったらC_odd_diffを1増やす
C_odd_diff,C_even_diff = 0,0

ans = 0
for i in range(Q):
    if S[i][0] == 1:
        if S[i][1] % 2 == 0:
            if C_even[S[i][1]//2-1] - C_even_diff >= S[i][2]:
                C_even[S[i][1]//2-1] -= S[i][2]
                ans += S[i][2]
                C_even_min = min(C_even[S[i][1]//2-1] - C_even_diff , C_even_min)
        else:
            if C_odd[(S[i][1]-1)//2] - C_odd_diff >= S[i][2]:
                C_odd[(S[i][1]-1)//2] -= S[i][2]
                ans += S[i][2]
                C_odd_min = min(C_odd[S[i][1]//2-1] - C_odd_diff , C_odd_min)
    if S[i][0] == 2:
        if C_odd_min >= S[i][1]:
            C_odd_diff += S[i][1]
            ans += len(C_odd)*S[i][1]
            C_odd_min -= S[i][1]
    if S[i][0] == 3:
        if C_odd_min >= S[i][1] and C_even_min >= S[i][1]:
            C_odd_diff += S[i][1]
            C_even_diff += S[i][1]
            ans += N*S[i][1]
            C_odd_min -= S[i][1]
            C_even_min -= S[i][1]

print(ans)
