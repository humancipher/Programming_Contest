INF = 10**6

n = int(input())
A = list(map(int,input().split()))
stk = [[INF,1]]
cnt = 0
Ans = []
for i in range(n):
    a = A[i]
    if stk[-1][0] != A[i]:
        stk.append([a,1])
    else:
        stk[-1][1] += 1
    cnt += 1
    if stk[-1][0] == stk[-1][1]:
        cnt -= stk[-1][1]
        stk.pop()
    Ans.append(cnt)
for i in range(len(Ans)):
    print(Ans[i])