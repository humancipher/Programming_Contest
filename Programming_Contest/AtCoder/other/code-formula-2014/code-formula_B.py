N = input()

even_sum,odd_sum = 0,0
for i in range(len(N)):
    if i % 2 == 0:
        even_sum += int(N[i])
    else:
        odd_sum += int(N[i])

if len(N) % 2 != 0:
    even_sum,odd_sum = odd_sum,even_sum

print(even_sum,odd_sum)
