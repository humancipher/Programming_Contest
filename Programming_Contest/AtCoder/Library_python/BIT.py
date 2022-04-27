class BIT:
    def __init__(self,n):
        self.Data = [0] * (n+1)
        self.n = n
    def plus(self,i,x):
        i += 1
        while i < self.n+1:
            self.Data[i] += x
            i += i&(-i)
    def subque(self,i): #[0,i]の和
        i += 1
        ans = 0
        while i > 0:
            ans += self.Data[i]
            i -= i&(-i)
        return ans
    def query(self,left,right): #[left,right]の和
        return self.subque(right)-self.subque(left-1)