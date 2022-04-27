n = int(input())
a,b = map(int,input().split())
if n <= a:
    ans = "Takahashi"
else:
    if a == b:
        if n % (a+1) == 0:
            ans = "Aoki"
        else:
            ans = "Takahashi"
    elif a < b:
        ans = "Aoki"
    else:
        ans = "Takahashi"
print(ans)