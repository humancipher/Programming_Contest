def score(A,ura):
    ans = 0
    for a in range(1,10):
        if a == ura:
            ans += a * pow(10,A[a]+1)
        else:
            ans += a * pow(10,A[a])
    return ans

def solve(S,T,K):
    C = dict()
    for i in range(1,10):
        C[i] = K
    for s in S:
        C[s] -= S[s]
    for t in T:
        C[t] -= T[t]
    
    ans = 0 #Sを持つ高橋の勝率
    for i in range(1,10):
        for j in range(1,10):
            if i == j:
                if C[i] >= 2:
                    if score(S,i) > score(T,j):
                        ans += C[i]*(C[j]-1)/((9*K-8)*(9*K-9))
            else:
                if C[i] >= 1 and C[j] >= 1:
                    if score(S,i) > score(T,j):
                        ans += C[i]*C[j]/((9*K-8)*(9*K-9))
    return ans

def main():
    K = int(input())
    S = list(input())
    T = list(input())
    SC,TC = dict(),dict()
    for i in range(1,10):
        SC[i] = 0
        TC[i] = 0
    for i in range(4):
        SC[int(S[i])] += 1
        TC[int(T[i])] += 1
    print(solve(SC,TC,K))

if __name__ == "__main__":
    main()
