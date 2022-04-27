n = int(input())
H = list(map(int,input().split()))
ans = H[0]
for i in range(1,n):
    if ans < H[i]:
        ans = H[i]
    else:
        break
print(ans)