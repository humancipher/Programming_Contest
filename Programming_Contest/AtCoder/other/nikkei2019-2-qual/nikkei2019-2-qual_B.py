from collections import Counter

def cal(D,M):
    C = Counter(D)
    MC = C.most_common()
    MC.sort(key = lambda x:x[0])
    n = len(MC)
    #頂点1が根じゃないときも連結の仕方を変えずに見方を変えることで
    #頂点1を根にできる.
    #従ってD[i-1]は頂点iの深さと見なせる
    for i in range(n):
        if MC[i][0] != i:
            #深さiと深さi-1又は深さiと深さi+1を繋げない
            return 0
    if MC[0][1] != 1 or D[0] != 0:
        #1以外の根がある又は1が根になってない
        return 0

    output = 1
    for i in range(n-1):
        output *= pow(MC[i][1],MC[i+1][1],M)
        output %= M
    return output

def main():
    N = int(input())
    D = list(map(int,input().split()))
    M = 998244353

    ans = cal(D,M)
    print(ans)

if __name__ == "__main__":
    main()
