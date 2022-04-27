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
