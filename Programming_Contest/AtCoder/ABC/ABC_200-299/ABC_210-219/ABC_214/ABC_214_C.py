n = int(input())
S = list(map(int,input().split()))
T = list(map(int,input().split()))

Ans = [T[i] for i in range(n)]
for i in range(2*n):
    Ans[i%n] = min(Ans[i%n],Ans[(i-1)%n]+S[(i-1)%n])

for i in range(n):
    print(Ans[i])