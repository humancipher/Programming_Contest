from heapq import heapify,heappush,heappop

S = input()
Al = [0]*26

for i in range(len(S)):
    Al[ord(S[i])-ord("a")] += 1
even,Odd = 0,[]
for i in range(26):
    if Al[i] % 2 == 0:
        even += Al[i]
    else:
        Odd.append(1)
        even += Al[i]-1
if len(Odd) == 0:
    print(len(S))
else:
    heapify(Odd)
    while even > 0:
        od = heappop(Odd)
        heappush(Odd,od+2)
        even -= 2
    od = heappop(Odd)
    print(od)