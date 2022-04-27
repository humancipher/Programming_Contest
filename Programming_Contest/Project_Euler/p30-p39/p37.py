from math import sqrt

def isPrime(n):
    for i in range(2,int(sqrt(n))+1):
        if n % i == 0:
            return False
    if n != 1:
        return True
    else:
        return False

def judge_left(p):
    p = str(p)
    for i in range(len(p)):
        if not isPrime(int(p[i:])):
            return False
    return True

def main():
    #pが右切り詰め可能素数:pがd桁としてint(p[i:])(0<=i<=d-1)が全て素数
    #pが左切り詰め可能素数:pがd桁としてint(p[:i+1])(0<=i<=d-1)が全て素数
    #pが切り詰め可能素数:pが切り右切り詰め可能素数且つ左切り詰め可能素数
    #よってd桁の右切り詰め可能素数のリストに1桁の数を右から繋げたやつしか
    #d+1桁の右切り詰め可能素数にならない
    #左切り詰め可能素数の場合はそうはいかないためか
    #左切り詰め可能素数は右切り詰め可能素数より多いようだ
    #従って右切り詰め可能素数のリストをつくり, それが左切り詰め可能素数かどうかを
    #確認するのがよさそうだ
    S,P_d = ["1","2","3","4","5","6","7","8","9"],["2","3","5","7"]
    P_d_r = [2,3,5,7]
    #右切り詰め可能素数
    digit = 1
    while len(P_d) > 0:
        P_d_next = []
        for p in P_d:
            for s in S:
                if isPrime(int(p+s)):
                    P_d_next.append(p+s)
                    P_d_r.append(int(p+s))
        P_d = P_d_next

    P = []
    for p in P_d_r:
        if judge_left(p):
            P.append(p)
    print(sum(P)-2-3-5-7)

if __name__ == "__main__":
    main()
