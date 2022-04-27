class ST: #セグメント木、i番目のxへの更新とmin(a[i:j])の計算をO(log(len(a)))で
    def __init__(self,N):
        self.INF = 1 << 60
        length = 1
        while length < N:
            length *= 2
        self.S = [self.INF] * (2 * length - 1)
        self.N = length
    
    def upd(self,x,i): #a[i]をxに更新
        pt = self.N - 1 + i #葉はS[N-1:2*N-2]
        self.S[pt] = x
        while pt > 0:
            par = (pt-1) // 2 #ptの親
            self.S[par] = min(self.S[2 * par + 1],self.S[2 * par + 2]) #ここは処理したい区間クエリによって変える
            pt = par
    
    def que(self,i,j): #min(a[i:j]の計算)
        return self.subque(i,j+1,0,self.N,0) #後ろは開区間なのでj+1
    
    def subque(self,i,j,left,right,pt): #S[pt]が見てる範囲がa[left:right]
        #最初にleftを左端、rightを右端にするので絞り込みのときに常にleft <= i and j <= rightになる
        if i >= j:
            return self.INF
        elif i == left and j == right:
            return self.S[pt]
        else:
            mid = (left + right) // 2
            return min(self.subque(i,min(mid,j),left,mid,2 * pt + 1),
                       self.subque(max(i,mid),j,mid,right,2 * pt + 2))
    
