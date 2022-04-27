class RMQ: #Range Max Queryに対応するセグメント木
    def __init__(self,n):
        beki = 1
        while beki < n:
            beki *= 2
        self.Data = [0] * (2*beki-1)
        self.beki = beki
        self.INF = 10**20
    def change(self,i,x): #i番目をxにする
        i += self.beki-1
        self.Data[i] = x
        while i > 0:
            i = (i-1)//2
            self.Data[i] = max(self.Data[2*i+1],self.Data[2*i+2])
    def query(self,left,right): #[left:right)でのmax
        stk = [] #pypyだと再帰関数が遅いのでスタックで実装する
        lower,upper = 0,self.beki
        ans = -self.INF
        stk.append((lower,upper,left,right,0))
        while len(stk) > 0:
            lower,upper,left,right,pt = stk.pop()
            if left <= lower and right >= upper: #はみ出しなし
                ans = max(ans,self.Data[pt])
            else:
                mid = (lower+upper)//2
                if mid > left: #重なりあり
                    stk.append((lower,mid,left,right,2*pt+1))
                if mid < right: #重なりあり
                    stk.append((mid,upper,left,right,2*pt+2))
        return ans