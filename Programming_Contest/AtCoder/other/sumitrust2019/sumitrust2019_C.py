X = int(input())

a,b = X // 100, X % 100
if b <= 5 * a:
    print(1)
else:
    print(0)
