n = int(input())
E = []
for _ in range(n):
    a,b = map(int,input().split())
    E.append([a,b,a+b])
E.sort(key = lambda x:x[2])
TA = [0,0]
for i in range(n):
    ABC = E.pop()
    TA[i%2] += ABC[i%2]
print(TA[0]-TA[1])