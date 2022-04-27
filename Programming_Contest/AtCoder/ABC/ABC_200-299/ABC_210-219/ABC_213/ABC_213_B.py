n = int(input())
A = list(map(int,input().split()))
B = [[A[i],i+1] for i in range(n)]
B.sort(key = lambda x:x[0])
print(B[n-2][1])
