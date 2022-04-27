N,K = map(int,input().split())
x = list(map(int,input().split()))
INF = 3*10**8+1

x_plus,x_minus,x_zero = [],[],0
for i in range(N):
    if x[i] < 0:
        x_minus.append(x[i])
    elif x[i] == 0:
        x_zero += 1
    else:
        x_plus.append(x[i])
for i in range(len(x_minus)//2):
    x_minus[i],x_minus[len(x_minus)-i-1] = x_minus[len(x_minus)-i-1],x_minus[i]

ans = INF
if 0 <= K-1-x_zero and K-1-x_zero < len(x_plus):
    ans = min(ans,x_plus[K-1-x_zero])
if 0 <= K-1-x_zero and K-1-x_zero < len(x_minus):
    ans = min(ans,-x_minus[K-1-x_zero])
for i in range(K):
    if i < len(x_plus) and 0 <= K-i-2-x_zero and K-i-2-x_zero < len(x_minus):
        tmp1 = 2*x_plus[i]-x_minus[K-i-2-x_zero]
        tmp2 = x_plus[i]-2*x_minus[K-i-2-x_zero]
        ans = min(ans,tmp1,tmp2)
if ans == INF:
    ans = 0
print(ans)
