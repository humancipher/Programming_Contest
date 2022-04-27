a,b = map(int,input().split())

ans = "No"
for c in range(1,3):
    if a*b*c % 2 == 1:
        ans = "Yes"
        break

print(ans)
