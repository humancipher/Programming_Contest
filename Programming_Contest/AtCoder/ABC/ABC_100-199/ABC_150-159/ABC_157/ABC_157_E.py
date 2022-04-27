class RMQ:
    def __init__(self,n):
        beki = 1
        while beki < n:
            beki *= 2
        self.Data = [0] * (2*beki-1)
        self.beki = beki
    def change(self,i,x): #i番目をxにする
        i += self.beki-1
        self.Data[i] = x
        while i > 0:
            i = (i-1)//2
            self.Data[i] = max(self.Data[2*i+1],self.Data[2*i+2])
    def query(self,left,right): #[left:right)でのmax
        stk = []
        lower,upper = 0,self.beki
        ans = 0
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

def main():
    import sys
    sys.stdin.readline
    n = int(input())
    rmq = [RMQ(n) for _ in range(26)] #rmq[i]:i番目のアルファベットの書き込みを管理したい
    S = list(input())
    for i in range(n):
        rmq[ord(S[i])-ord("a")].change(i,1)
    q = int(input())
    Ans = []
    for _ in range(q):
        a,b,c = input().split()
        a,b = int(a),int(b)
        if a == 1:
            if S[b-1] != c:
                rmq[ord(S[b-1])-ord("a")].change(b-1,0)
                rmq[ord(c)-ord("a")].change(b-1,1)
                S[b-1] = c
        else:
            c = int(c)
            cnt = 0
            for i in range(26):
                if rmq[i].query(b-1,c) == 1: #i番目のアルファベットヒット
                    cnt += 1
            Ans.append(cnt)
    for i in range(len(Ans)):
        print(Ans[i])

if __name__ == "__main__":
    main()
