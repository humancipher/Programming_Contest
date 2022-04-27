A,V = map(int,input().split())
B,W = map(int,input().split())
T = int(input())

if A > B:
    A,B = B,A

if A + V * T >= B + W * T:
    print("YES")
else:
    print("NO")
