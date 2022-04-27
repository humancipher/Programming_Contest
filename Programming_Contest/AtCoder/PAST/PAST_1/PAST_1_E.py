class SNS:
    #(V,E) = (ユーザー,フォロー)
    #e = (a,b):ユーザaがユーザbをフォロー
    def __init__(self,V,E):
        self.V = V
        self.E = E

    def follow(self,a,b):
        self.E.add((a,b))

    def follow_back(self,a):
        E_ = set()
        for (e1,e2) in self.E:
            if e2 == a:
                E_.add((e2,e1))
        self.E = self.E | E_

    def follow_follow(self,a):
        E_,E_a = set(),set()
        for (e1,e2) in self.E:
            if e1 == a:
                E_a.add((e1,e2))
        for e3 in range(1,self.V+1):
            for (e1,e2) in E_a:
                if (e2,e3) in self.E and e1 != e3:
                    E_.add((e1,e3))
        self.E = self.E | E_

    def follow_print(self):
        for i in range(1,self.V+1):
            output = ""
            for j in range(1,self.V+1):
                if (i,j) in self.E:
                    output += "Y"
                else:
                    output += "N"
            print(output)

N,Q = map(int,input().split())
S = [list(map(int,input().split())) for _ in range(Q)]

sns = SNS(N,set())

for i in range(Q):
    if S[i][0] == 1:
        sns.follow(S[i][1],S[i][2])
    elif S[i][0] == 2:
        sns.follow_back(S[i][1])
    elif S[i][0] == 3:
        sns.follow_follow(S[i][1])

sns.follow_print()
