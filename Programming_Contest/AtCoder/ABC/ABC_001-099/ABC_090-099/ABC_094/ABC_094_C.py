N = int(input())
X = list(map(int,input().split()))

Y = sorted(X)

Y_mid_left,Y_mid_right = Y[N//2-1],Y[N//2]

for i in range(N):
    if X[i] <= Y_mid_left:
        print(Y_mid_right)
    else:
        print(Y_mid_left)
