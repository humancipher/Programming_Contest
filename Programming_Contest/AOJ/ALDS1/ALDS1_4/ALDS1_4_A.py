n = int(input())
S = [int(x) for x in input().split()]
q = int(input())
T = [int(x) for x in input().split()]

def LinearSearch(S,T):
    count = 0
    for i in range(q): #T
        for j in range(n): #S
            if T[i] == S[j]:
                count += 1
                break
    return count

print(LinearSearch(S,T))
