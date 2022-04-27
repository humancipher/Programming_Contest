INF = 10**6

class RMQ:
    def __init__(self,_n):
        n = 1
        while n < _n:
            n *= 2
        self.A = [0] * (2*n-1)
        self.n = n
    def update(self,i,x):
        i += self.n-1
        self.A[i] = x
        while i > 0:
            par = (i-1)//2
            self.A[par] = max(self.A[2*par+1],self.A[2*par+2])
            i = par
    def query(self,a,b):
        #return self.subque(l,r,0,self.n,0)
        l,r = 0,self.n
        ans = -INF
        stk = [(l,r,0)]
        while len(stk) > 0:
            x,y,pt = stk.pop()
            if x >= a and y <= b:
                ans = max(ans,self.A[pt])
            elif y <= a or x >= b:
                continue
            else:
                mid = (x+y)//2
                stk.append((x,mid,2*pt+1))
                stk.append((mid,y,2*pt+2))
        return ans

def main():
    lng = 3*10**5+1
    n,k = map(int,input().split())
    dp = RMQ(lng) #dp[i]:末尾がiになる最大長
    A = [int(input()) for _ in range(n)]
    for i in range(n):
        a = A[i]
        al = max(0,a-k)
        ar = min(lng,a+k+1)
        upd = dp.query(al,ar)
        dp.update(a,upd+1)
    print(max(dp.A))

if __name__ == "__main__":
    main()
