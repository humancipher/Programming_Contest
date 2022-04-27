N = int(input())
C = [x for x in input().split()]

def BubbleSort(C):
    N = len(C)
    for i in range(N):
        for j in reversed(range(i+1,N)):
            if C[j][1] < C[j-1][1]:
                C[j], C[j-1] = C[j-1], C[j]
    return C

def SelectionSort(C):
    N = len(C)
    for i in range(N):
        minj = i
        for j in range(i,N):
            if C[j][1] < C[minj][1]:
                minj = j
        C[i], C[minj] = C[minj], C[i]
    return C

D1 = C[:]
#注：D1 = Cだと参照渡しになる. つまり, D1を変更するとCも変更される
#C[:]を代入すると値渡しになる.
D1 = BubbleSort(D1)
for i in range(N-1):
    print(D1[i], end=" ")
print(D1[N-1])
print("Stable")

D2 = C[:]
D2 = SelectionSort(D2)
for i in range(N-1):
    print(D2[i], end=" ")
print(D2[N-1])
if D1 ==D2:
    print("Stable")
else:
    print("Not stable")
