a = int(input())
b = int(input())

if b % 2 == 0:
    ans = str(a) + str(b//2)
else:
    b *= 10
    ans = str(a) +"0"+ str(b//2)
print(ans)