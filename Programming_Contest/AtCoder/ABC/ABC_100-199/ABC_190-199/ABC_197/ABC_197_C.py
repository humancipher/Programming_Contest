INF = 2 << 32

def XOR(A):
    ans = 0
    for a in A:
        ans ^= a
    return ans

def OR(A):
    ans = 0
    for a in A:
        ans |= a
    return ans

def solve(A,N):
    ans = INF
    for i in range(2**N):
        left = 0
        tmp = []
        for j in range(N):
            if 2**j & i:
                tmp.append(OR(A[left:j])) 
                left = j
        tmp.append(OR(A[left:N]))
        ans = min(ans,XOR(tmp))
    return ans

def main():
    N = int(input())
    A = list(map(int,input().split()))
    print(solve(A,N))

if __name__ == "__main__":
    main()
