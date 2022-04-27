class BIT:
    def __init__(self,n):
        self.Data = [0] * (n+1)
        self.n = n
    def plus(self,i,x):
        i += 1
        while i <= self.n:
            self.Data[i] += x
            i += i&(-i)
    def subque(self,i):
        i += 1
        ans = 0
        while i > 0:
            ans += self.Data[i]
            i -= i&(-i)
        return ans
    def query(self,left,right):
        return self.subque(right)-self.subque(left-1)

def main():
    n,q = map(int,input().split())
    A = list(map(int,input().split()))
    bit = BIT(n)
    for i in range(n):
        bit.plus(i,A[i])
    Ans = list()
    for _ in range(q):
        a,b,c = map(int,input().split())
        if a == 0:
            bit.plus(b,c)
        else:
            ans = bit.query(b,c-1)
            Ans.append(ans)
    for i in range(len(Ans)):
        print(Ans[i])

if __name__ == "__main__":
    main()
