a,b = input().split()

if len(a) < len(b):
    a = "0"*(len(b)-len(a)) + a
else:
    b = "0"*(len(a)-len(b)) + b

ans = "Easy"
for i in range(len(a)):
    if int(a[i]) + int(b[i]) >= 10:
        ans = "Hard"
        break
print(ans)
