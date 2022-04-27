n = int(input())
S = set()
for _ in range(n):
    LA = list(map(int,input().split()))
    LA = tuple(LA[1:])
    S.add(LA)
print(len(S))