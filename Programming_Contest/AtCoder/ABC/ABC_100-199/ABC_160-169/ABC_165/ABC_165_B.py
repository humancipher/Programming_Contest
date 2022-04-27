x = int(input())

count,money = 0,100
while money < x:
    money = int(1.01*money)
    count += 1

print(count)
