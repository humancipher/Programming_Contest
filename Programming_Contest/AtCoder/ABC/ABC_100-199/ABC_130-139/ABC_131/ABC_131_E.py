n,k = map(int,input().split())
if (n-1)*(n-2)//2 - k < 0:
    print(-1)
else:
    G = [[0] * n for _ in range(n)]
    for i in range(1,n):
        G[0][i] = 1
    cnt = (n-1)*(n-2)//2 - k
    for i in range(1,n):
        if cnt > 0:
            for j in range(i+1,n):
                G[i][j] = 1
                cnt -= 1
                if cnt == 0:
                    break
        else:
            break
    Ans = []
    for i in range(n):
        for j in range(n):
            if G[i][j] == 1:
                Ans.append((i+1,j+1))
    print(len(Ans))
    for i in range(len(Ans)):
        print(Ans[i][0],Ans[i][1])
