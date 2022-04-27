n = int(input())
a,b,c = map(int,input().split())

ans = 9999
for i in range(9999):
    for j in range(9999-i):
        if a*i+b*j <= n:
            if (n - (a*i+b*j)) % c == 0:
                ans = min(ans,i+j+(n-(a*i+b*j))//c)
        else:
            break

print(ans)
