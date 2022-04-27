N = int(input())
A = [int(x) for x in input().split()]

AB = [(A[i],i) for i in range(N)]

AB.sort(key = lambda x:x[0])

B = [AB[i][1]+1 for i in range(N)]

ans = " ".join(map(str,B))
print(ans)
