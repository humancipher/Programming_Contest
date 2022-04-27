N,M,X,Y = map(int,input().split())
x = list(map(int,input().split()))
y = list(map(int,input().split()))

x.sort()
y.sort()

if max(X,x[N-1]) < min(Y,y[0]):
    print("No War")
else:
    print("War")
