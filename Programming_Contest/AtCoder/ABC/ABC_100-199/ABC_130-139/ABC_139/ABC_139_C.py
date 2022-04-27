N = int(input())
H = [int(x) for x in input().split()]

max, count = 0, 0
for i in range(N-1):
    if H[i] >= H[i+1]:
        count += 1
    else:
        count = 0
    if max < count:
        max = count

print(max)
