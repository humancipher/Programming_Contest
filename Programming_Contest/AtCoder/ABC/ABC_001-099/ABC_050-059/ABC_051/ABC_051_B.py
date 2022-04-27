K,S = map(int,input().split())

count = 0
if S % 3 == 0:
    count += 1
for x in range(K):
    if 0 <= S-2*x and S-2*x <= K and x != S-2*x:
        count += 3
for x in range(K):
    for y in range(x+1,K):
        if y >= S-x-y:
            break
        elif 0 <= S-x-y and S-x-y <= K:
            count += 6

print(count)
