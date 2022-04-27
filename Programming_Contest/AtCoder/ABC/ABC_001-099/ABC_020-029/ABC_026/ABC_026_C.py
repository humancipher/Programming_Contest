N = int(input())
B = [int(input()) for _ in range(N-1)]

buka = [[] for _ in range(N+1)]
#buka[i]:社員iの直属の部下
for i in range(N-1):
    buka[B[i]].append(i+2)

sal = [0 for i in range(N+1)]
INF = 10**9
for i in reversed(range(1,N+1)):
    if len(buka[i]) == 0:
        sal[i] = 1
    else:
        max_sal,min_sal = 0,INF
        for b in buka[i]:
            max_sal,min_sal = max(max_sal,sal[b]),min(min_sal,sal[b])
        sal[i] = max_sal+min_sal+1

print(sal[1])
