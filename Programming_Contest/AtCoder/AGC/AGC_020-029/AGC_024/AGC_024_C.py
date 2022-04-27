def cal(A):
    ans = 0
    if A[0] != 0:
        return -1
    for i in range(len(A)-1):
        if A[i+1] == A[i]:
            ans += A[i+1]
        elif A[i+1]-1 == A[i]:
            ans += 1
        elif A[i+1] < A[i]:
            ans += A[i+1]
        else:
            return -1
    return ans

def main():
    import sys
    input = sys.stdin.readline
    n = int(input())
    A = [int(input()) for _ in range(n)]
    if A[0] != 0:
        ans = -1
    else:
        B = [[0]]
        for i in range(1,n):
            if A[i] != 0:
                B[-1].append(A[i])
            else:
                B.append([0])
        ans = 0
        for i in range(len(B)):
            tmp = cal(B[i])
            if tmp == -1:
                ans = -1
                break
            else:
                ans += tmp
    print(ans)

if __name__ == "__main__":
    main()
