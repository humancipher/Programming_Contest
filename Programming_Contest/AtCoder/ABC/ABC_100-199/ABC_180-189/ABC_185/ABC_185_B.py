N,M,T = map(int,input().split())
AB = [list(map(int,input().split())) for _ in range(M)]
A = [AB[i][0] for i in range(M)]
B = [AB[i][1] for i in range(M)]
A = [0] + A
B = [0] + B
ans = "Yes"
tmp = N
for i in range(1,M+1):
    tmp -= (A[i] - B[i-1])
    if tmp <= 0:
        ans = "No"
        break
    tmp += (B[i] - A[i])
    tmp = min(tmp,N)

tmp -= T - B[-1]
if tmp <= 0:
    ans = "No"

print(ans)
