def solve(A,N):
    C = dict() #C[a]:カードaの枚数
    T = [] #T[i]:i番目に小さいカードの数値
    for a in A:
        if a in C:
            C[a] += 1
        else:
            C[a] = 1
            T.append(a)
    T.sort()
    left,right = 0,len(T)-1
    ans = N
    while True:
        if C[T[left]] <= 1:
            while C[T[left]] <= 1 and left < right:
                left += 1
        if C[T[right]] <= 1:
            while C[T[right]] <= 1 and left < right:
                right -= 1
        if left < right:
            C[T[left]] -= 1
            C[T[right]] -= 1
            ans -= 2
        else:
            if C[T[left]] % 2 == 0:
                ans -= C[T[left]]
            else:
                ans -= (C[T[left]] - 1)
            break
    return ans

def main():
    N = int(input())
    A = list(map(int,input().split()))
    print(solve(A,N))

if __name__ == "__main__":
    main()
