def Array_list(array_list,m,n):
    if n == 0:
        return array_list
    else:
        array_list_next = []
        for array in array_list:
            for i in range(array[len(array)-1],m+1):
                array_list_next.append(array+[i])
        return Array_list(array_list_next,m,n-1)

def main():
    N,M,Q = map(int,input().split())
    abcd = [list(map(int,input().split())) for _ in range(Q)]

    L = [[i] for i in range(1,M+1)]
    array_list = Array_list(L,M,N)

    ans,tmp = 0,0
    for array in array_list:
        tmp = 0
        for a,b,c,d in abcd:
            if array[b-1] - array[a-1] == c:
                tmp += d
        ans = max(tmp,ans)

    print(ans)

if __name__ == "__main__":
    main()
