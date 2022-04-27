INF = 10**11

from bisect import bisect_left

S = input()
k = int(input())

C = [0] * (len(S))
for i in range(len(S)):
    if S[i] == ".":
        C[i] = 1
for i in range(1,len(S)):
    C[i] += C[i-1]

C.append(INF) #番兵
ans = bisect_left(C,k+1)
for i in range(1,len(S)):
    j = bisect_left(C,k+C[i-1]+1)
    ans = max(ans,j-i)
print(ans)