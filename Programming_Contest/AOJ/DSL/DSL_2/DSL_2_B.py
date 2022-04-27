class RSQ:
    def __init__(self,_n):
        n = 1
        while n < _n:
            n *= 2
        self.n = n
        self.L = [0] * (2*n-1)
    def add(self,i,x):
        i += self.n-1
        self.L[i] += x
        while i > 0:
            par = (i-1)//2
            self.L[par] = self.L[2*par+1] + self.L[2*par+2]
            i = par
    def getsum(self,s,t):
        return self.subgetsum(s,t+1,0,self.n,0)
    def subgetsum(self,s,t,a,b,k):
        if s <= a and t >= b:
            return self.L[k]
        elif s >= b or t <= a:
            return 0
        else:
            return self.subgetsum(s,t,a,(a+b)//2,2*k+1) \
                    + self.subgetsum(s,t,(a+b)//2,b,2*k+2)
        
n,q = map(int,input().split())
rsq = RSQ(n)
for _ in range(q):
    com,x,y = map(int,input().split())
    if com == 0:
        rsq.add(x-1,y)
    else:
        print(rsq.getsum(x-1,y-1))
