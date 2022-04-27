N,Q = map(int,input().split())
S = list(input())
S = ["_"]+S
LR = [tuple(map(int,input().split())) for _ in range(Q)]

C = [0 for _ in range(N+1)]
#C[i]:i文字目までで"AC"が出てくる回数
for i in range(1,N):
    if S[i] == "A" and S[i+1] == "C":
        C[i+1] += 1

for i in range(N):
    C[i+1] += C[i]


for l,r in LR:
    print(C[r]-C[l])
