n = int(input())
A = list(map(int,input().split()))
B = list(map(int,input().split()))
small = max(A)
big = min(B)
print(max(0,big-small+1))
