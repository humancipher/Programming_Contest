A,B,W = map(int,input().split())
W *= 1000
INF = 10**7

ans_min,ans_max = INF,0
for i in range(10**6+1):
    if A*i <= W <= B*i:
        if ans_min == INF:
            ans_min = i
        ans_max = i
if ans_min == INF:
    print("UNSATISFIABLE")
else:
    print(ans_min,ans_max)
