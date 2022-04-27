def replace(n,r):
    m = n*r
    m,n = list(str(m)),list(str(n))
    m.sort()
    n.sort()
    if m == n:
        return True
    else:
        return False

def main():
    #最上位桁が1以外だと6倍したときに桁数が1多くなる
    #3倍したら3の倍数になるから格桁の和が3の倍数になる
    #よって3の倍数しか3倍したときに置換倍数にならない
    digit = 1
    get_ans = False
    digit_limit = 7
    while not get_ans and digit < digit_limit:
        n = 10**digit + 2
        n_lim = 10**(digit+1)//6
        #n * 6 < 10**(digit+1)
        while n <= 10**(digit+1)//6:
            get_ans = True
            for i in range(1,7):
                if not replace(n,i):
                    get_ans = False
                    break
            if get_ans:
                ans = n
                break
            else:
                n += 3
        if not get_ans:
            digit += 1

    if digit < digit_limit:
        print(ans)
    else:
        print("over")

if __name__ == "__main__":
    main()
