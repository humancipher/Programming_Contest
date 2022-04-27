n,a = map(int,input().split())
k = int(input())
B = list(map(int,input().split()))
a -= 1
for i in range(n):
    B[i] -= 1

if k <= n:
    while k > 0:
        a = B[a]
        k -= 1
    ans = a + 1
else:
    Loop,S = list(),set()
    a = B[a]
    for i in range(n):
        if a not in S:
            Loop.append(a)
            S.add(a)
            a = B[a]
        else:
            break
    for j in range(len(Loop)):
        if Loop[j] == a:
            left = j
            break
    k -= left
    amari = k % (len(Loop)-left)
    ans = Loop[left+amari-1] + 1
print(ans)
