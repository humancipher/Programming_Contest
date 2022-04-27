N = int(input())
A,B = map(int,input().split())
C = int(input())
D = [int(input()) for _ in range(N)]

D.sort(reverse = True)

cal,money,pt = C,A,0
for pt in range(N):
    #if cal / money <= (cal+D[pt]) / (money + B):
    if cal * (money + B) <= (cal + D[pt]) * money:
        cal += D[pt]
        money += B
        pt += 1
    else:
        break

print(int(cal/money))
