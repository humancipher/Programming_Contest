n = int(input())
ST = [list(input().split()) for _ in range(n)]
for i in range(n):
    ST[i][1] = int(ST[i][1])
ST.sort(key = lambda x:x[1])
print(ST[-2][0])
