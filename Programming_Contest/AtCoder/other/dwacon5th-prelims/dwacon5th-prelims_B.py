n,k = map(int,input().split())
A = list(map(int,input().split()))

A = [0] + A
for i in range(len(A)-1):
    A[i+1] += A[i]
Arui = []
for i in range(len(A)):
    for j in range(i+1,len(A)):
        Arui.append(A[j]-A[i])

B = [set() for _ in range(40)]
for i in range(len(Arui)):
    for j in range(40):
        if Arui[i] & 2**j:
            B[j].add(i)

ans = 0
Now = set([i for i in range(len(Arui))])
for i in reversed(range(40)):
    Next = set()
    for b in B[i]:
        if b in Now:
            Next.add(b)
    if len(Next) >= k:
        ans += 2**i
        Now = Next
print(ans)