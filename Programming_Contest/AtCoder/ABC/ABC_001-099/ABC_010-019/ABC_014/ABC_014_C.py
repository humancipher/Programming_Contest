n = int(input())
C = [0 for _ in range(10**6+2)]
for _ in range(n):
    a,b = map(int,input().split())
    C[a] += 1
    C[b+1] -= 1

for i in range(1,10**6+2):
    C[i] += C[i-1]
print(max(C))
