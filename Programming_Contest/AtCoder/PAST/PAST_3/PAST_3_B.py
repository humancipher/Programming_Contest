def operate(S,N,M,Q):
    Solve = [set() for _ in range(N+1)]
    #Score[i]:参加者iが解いた問題の集合
    Solver = [set() for _ in range(M+1)]
    #Solver[i]:問題iを解いた参加者の集合
    for i in range(Q):
        if S[i][0] == 1:
            n = S[i][1]
            score = 0
            for q in Solve[n]:
                score += (N-len(Solver[q]))
            print(score)
        else:
            n,m = S[i][1],S[i][2]
            Solve[n].add(m)
            Solver[m].add(n)

def main():
    N,M,Q = map(int,input().split())
    S = [list(map(int,input().split())) for _ in range(Q)]

    operate(S,N,M,Q)

if __name__ == "__main__":
    main()
