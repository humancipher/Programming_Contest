N,X = map(int,input().split())
S = input()

for i in range(N):
    if S[i] == "o":
        X += 1
    else:
        X = max(0,X-1)

print(X)
