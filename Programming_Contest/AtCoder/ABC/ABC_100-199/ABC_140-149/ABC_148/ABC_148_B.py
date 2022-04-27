N = int(input())
S, T = input().split()

L = ""
for i in range(N):
    L = L + S[i] + T[i]

print(L)
