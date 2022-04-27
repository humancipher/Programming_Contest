n = int(input())
S = [int(x) for x in input().split()]
q = int(input())
T = [int(x) for x in input().split()]

def BinarySearch(S,T):
    count = 0
    for i in range(q):
        left = 0
        right = n
        #right = n-1だとヒットするのがS[n-1]のみのときに見つからない
        #left < rightとmidは切り捨てより常にmid < right
        while left < right:
            mid = int((left + right) / 2)
            if T[i] == S[mid]:
                count += 1
                break
            elif T[i] < S[mid]:
                right = mid
            else:
                left = mid + 1
    return count

print(BinarySearch(S,T))
