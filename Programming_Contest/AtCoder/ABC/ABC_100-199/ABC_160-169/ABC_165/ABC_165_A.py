K = int(input())
A,B = map(int,input().split())

flag = False
for i in range(A,B+1):
    if i % K == 0:
        print("OK")
        flag = True
        break

if not flag:
    print("NG")
