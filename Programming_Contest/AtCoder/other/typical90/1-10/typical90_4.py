h,w = map(int,input().split())
A = [list(map(int,input().split())) for _ in range(h)]
Tate = [0 for _ in range(w)]
Yoko = [0 for _ in range(h)]
for i in range(h):
    for j in range(w):
        Tate[j] += A[i][j]
        Yoko[i] += A[i][j]
Ans = [[0 for _ in range(w)] for _ in range(h)]
for i in range(h):
    for j in range(w):
        Ans[i][j] = Yoko[i]+Tate[j]-A[i][j]
for i in range(h):
    print(" ".join(map(str,Ans[i])))
