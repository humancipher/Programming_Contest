n,w = map(int,input().split())
AB = [list(map(int,input().split())) for _ in range(n)]

AB.sort(key = lambda x:x[0])
ans,tmp_w = 0,0
for i in reversed(range(n)):
    if tmp_w < w:
        add_w = min(AB[i][1],w-tmp_w)
        ans += AB[i][0] * add_w
        tmp_w += add_w
print(ans)
