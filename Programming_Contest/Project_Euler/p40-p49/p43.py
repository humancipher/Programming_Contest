#競プロならまだまた実行時間的にアウト
from itertools import permutations

def judge(n):
    n = str(n)
    d = [int(n[1+i:1+i+3]) for i in range(7)]
    P = [2,3,5,7,11,13,17]

    for i in reversed(range(7)):
        if d[i] % P[i] != 0:
            return False
    return True

def main():
    L = [str(i) for i in range(1,10)]
    P_ = list(permutations(L))
    P = []
    for p_ in P_:
        p_ = "".join(p_)
        for i in range(9):
            p = p_[:i+1] + "0" + p_[i+1:]
            if int(p[3]) % 2 == 0 and int(p[5]) % 5 == 0:
                P.append(int(p))

    ans = 0
    for p in P:
        if judge(p):
            ans += p

    print(ans)

if __name__ == "__main__":
    main()
