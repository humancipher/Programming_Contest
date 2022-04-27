S = list(input())
n = int(input())

for _ in range(n):
    l,r = map(int,input().split())
    for i in range(l-1,r):
        if i < r+l-2-i:
            S[i],S[r+l-2-i] = S[r+l-2-i],S[i]
print("".join(S))
