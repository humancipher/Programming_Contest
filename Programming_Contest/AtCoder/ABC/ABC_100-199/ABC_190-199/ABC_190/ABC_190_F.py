class BIT:
    def __init__(self,N):
        self.N = N
        self.A = [0 for _ in range(N+1)] #BITでは1番目を最初にすると実装しやすい
    
    def sum(self,n): #nsum(A[1:n+1])を計算（必要に応じてここを書き換えるとxor_sum等も実装できる）
        s = 0
        while n > 0:
            s += self.A[n] #ここを取りたい部分和の形式に併せて変える
            n -= n & (-n) #nのLSB
        return s
    
    def add(self,n,x): # n番目にxを足す
        if n > 0:
            while n <= self.N:
                self.A[n] += x
                n += n & (-n) # nのLSB

def init_reverse(A,N):
    bit = BIT(N)
    
    ans = 0
    for j in range(N):
        ans += j - bit.sum(A[j])
        bit.add(A[j],1)
    
    return ans

def main():
    N = int(input())
    A = list(map(int,input().split()))
    B = [A[i]+1 for i in range(N)]

    ans = init_reverse(B,N)
    print(ans)
    for i in range(N-1):
        ans += (N - 2 * A[i] - 1)
        print(ans)

if __name__ == "__main__":
    main()
