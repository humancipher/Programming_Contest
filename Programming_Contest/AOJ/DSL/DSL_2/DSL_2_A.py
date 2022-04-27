INF = 2**32
INIT = 2**31-1

class RMQ:
    def __init__(self,_n):
        self.n = 1
        while self.n < _n:
            self.n *= 2
        self.L = [INIT] * (2*self.n-1)
    def update(self,i,x):
        i += self.n-1
        self.L[i] = x
        while i > 0:
            self.L[(i-1)//2] = min(self.L[((i-1)//2)*2+1],self.L[((i-1)//2)*2+2])
            i = (i-1)//2
    def find_main(self,x,y,a,b,k): #[x,y)での最小値
        if x <= a and y >= b:
            return self.L[k]
        else:
            if x >= b or y <= a:
                return INF
            else:
                ans1 = self.find_main(x,y,a,(a+b)//2,2*k+1)
                ans2 = self.find_main(x,y,(a+b)//2,b,2*k+2)
                return min(ans1,ans2)
    def find(self,x,y):
        return self.find_main(x,y+1,0,self.n,0)

n,q = map(int,input().split())
rmq = RMQ(n)
for i in range(q):
    com,x,y = map(int,input().split())
    if com == 0:
        rmq.update(x,y)
    else:
        print(rmq.find(x,y))
