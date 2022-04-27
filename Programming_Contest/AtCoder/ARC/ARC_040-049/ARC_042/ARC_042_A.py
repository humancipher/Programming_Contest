N,M = map(int,input().split())
a = [int(input()) for _ in range(M)]

S = [[i+1,i+1] for i in range(N)]
#S[i][j]:スレッドiは上からj番目
#注:スレッドの順序は負の数も用いて表現し, 順序を知りたいときはソートする

for i in range(M):
    S[a[i]-1][1] = -i

S.sort(key = lambda x:x[1])

for i in range(N):
    print(S[i][0])
