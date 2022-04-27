from bisect import bisect_left,bisect_right

def D_stk(w,N):
    INF = 10**5+1
    stk_top_list = [INF]

    for i in range(N):
        bsl = bisect_left(stk_top_list,w[i])
        if bsl == len(stk_top_list):
            stk_top_list.append(w[i])
        else:
            stk_top_list[bsl] = w[i]
    
    return len(stk_top_list)

def main():
    N = int(input())
    w = [int(input()) for _ in range(N)]

    print(D_stk(w,N))

if __name__ == "__main__":
    main()
