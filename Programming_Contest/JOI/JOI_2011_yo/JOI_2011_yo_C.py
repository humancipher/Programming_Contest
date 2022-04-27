N = int(input())
K = int(input())
AB = [list(map(int,input().split())) for _ in range(K)]

for i in range(K):
    AB[i][0] = min(AB[i][0],N-AB[i][0]+1)-1
    AB[i][1] = min(AB[i][1],N-AB[i][1]+1)-1
    col_d = min(AB[i][0],AB[i][1])
    col = (col_d % 3)+1
    print(col)
