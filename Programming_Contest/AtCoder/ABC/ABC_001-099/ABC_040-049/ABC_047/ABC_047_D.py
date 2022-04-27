n,t = map(int,input().split())
A = list(map(int,input().split()))

Sel = [A[i] for i in range(n)]
for i in range(n-1):
    Sel[n-i-2] = max(Sel[n-i-2],Sel[n-i-1])
cnt,tmp_max = 0,0
for i in range(n-1):
    if tmp_max == Sel[i+1] - A[i]:
        cnt += 1
    elif tmp_max < Sel[i+1] - A[i]:
        tmp_max = Sel[i+1] - A[i]
        cnt = 1
print(cnt)