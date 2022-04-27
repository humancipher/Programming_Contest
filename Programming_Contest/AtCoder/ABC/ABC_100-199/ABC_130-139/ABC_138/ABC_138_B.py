N = int(input())
A = [int(x) for x in input().split()]

sum = 0
for a in A:
    sum += 1/a
print(1/sum)
