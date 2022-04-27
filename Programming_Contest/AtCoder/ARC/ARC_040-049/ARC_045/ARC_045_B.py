class RMQ:
    def __init__(self,n):
        self.INF = 10**6
        beki = 1
        while beki < n:
            beki *= 2
        self.Data = [self.INF] * (2*beki-1)
        self.beki = beki
    def update(self,pt,x): #pt番目をxに更新
        pt += self.beki-1
        self.Data[pt] = x
        while pt > 0:
            pt = (pt-1)//2
            self.Data[pt] = min(self.Data[2*pt+1],self.Data[2*pt+2])
    def query(self,left,right): #[left:right)でのmax
        stk = [] #pypyだと再帰関数が遅いのでスタックで実装する
        lower,upper = 0,self.beki
        ans = self.INF
        stk.append((lower,upper,left,right,0))
        while len(stk) > 0:
            lower,upper,left,right,pt = stk.pop()
            if left <= lower and right >= upper: #はみ出しなし
                ans = min(ans,self.Data[pt])
            else:
                mid = (lower+upper)//2
                if mid > left: #重なりあり
                    stk.append((lower,mid,left,right,2*pt+1))
                if mid < right: #重なりあり
                    stk.append((mid,upper,left,right,2*pt+2))
        return ans

def main():
    from itertools import accumulate
    import sys
    input = sys.stdin.readline
    n,m = map(int,input().split())
    A = [0] * n
    ST = []
    for _ in range(m):
        s,t = map(int,input().split())
        s,t = s-1,t-1
        ST.append((s,t))
        A[s] += 1
        if t+1 < n:
            A[t+1] -= 1
    A = list(accumulate(A))
    rmq = RMQ(n)
    for i in range(n):
        rmq.update(i,A[i])
    Ans = list()
    for i in range(m):
        s,t = ST[i][0],ST[i][1]
        if rmq.query(s,t+1) >= 2:
            Ans.append(i+1)
    print(len(Ans))
    for i in range(len(Ans)):
        print(Ans[i])
            
if __name__ == "__main__":
    main()
