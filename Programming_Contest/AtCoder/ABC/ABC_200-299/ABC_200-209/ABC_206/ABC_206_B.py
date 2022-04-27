n = int(input())

money,day = 0,0
while money < n:
    day += 1
    money += day
print(day)
