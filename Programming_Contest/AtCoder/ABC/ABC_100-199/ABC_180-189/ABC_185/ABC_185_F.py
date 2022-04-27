class BIT:
    def __init__(self,N):
        self.N = N
        self.A = [0 for _ in range(N+1)] #BITでは1番目を最初にすると実装しやすい
    
    def sum(self,n): #nsum(A[1:n+1])を計算（必要に応じてここを書き換えるとxor_sum等も実装できる）
        s = 0
        while n > 0:
            s ^= self.A[n] #ここを取りたい部分和の形式に併せて変える
            n -= n & (-n) #nのLSB
        return s
    
    def add(self,n,x): # n番目にxを足す
        if n > 0:
            while n <= self.N:
                self.A[n] ^= x
                n += n & (-n) # nのLSB

    def output(self,i,j): #sum(A[i:j+1])を出力する
        return self.sum(j) ^ self.sum(i-1)

def main():
    N,Q = map(int,input().split())
    bit = BIT(N)
    A = list(map(int,input().split()))
    for i in range(N):
        bit.add(i+1,A[i])
    Ans = []
    for _ in range(Q):
        t,x,y = map(int,input().split())
        if t == 1:
            bit.add(x,y)
        else:
            Ans.append(bit.output(x,y))
    for i in range(len(Ans)):
        print(Ans[i])

if __name__ == "__main__":
    main()
