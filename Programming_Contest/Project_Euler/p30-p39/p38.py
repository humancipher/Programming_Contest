def judge(n):
    n = list(str(n))
    for i in range(len(n)):
        n[i] = int(n[i])
    if len(n) == 9 and max(n) == 9 and min(n) == 1 and len(set(n)) == 9:
        return True
    else:
        return False

def main():
    #m*(1,2,...,n)(n>1)でnをうまく選んでできるパンデジタル数を最大化したい
    #9*(1,2,3,4,5)でパンデジタル数918273645を得る
    #最上位桁が9になるためにはまずmの最上位桁は9
    #mが2桁:ありえない(∵m*1が2桁,m*2以降が3桁になるから)
    #mが3桁:ありえない
    #mが4桁:あり得る
    #mが5桁以上:ありえない(m*1が5桁,m*2が6桁でn>1にならない)
    ans = 918273645
    for i in range(9123,9877):
        pand1,pand2 = str(i),str(i*2)
        pand = int(pand1+pand2)
        if judge(pand) and pand > ans:
            ans = pand

    print(ans)

if __name__ == "__main__":
    main()
