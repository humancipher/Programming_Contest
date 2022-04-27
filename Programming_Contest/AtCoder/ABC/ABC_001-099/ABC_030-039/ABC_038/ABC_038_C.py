def cont(a,N):
    OP = []
    a.append(0) #番兵
    st,sp,ep = a[0],0,None
    for i in range(1,N+1):
        if st < a[i]:
            st = a[i]
        else:
            ep = i-1
            OP.append((sp,ep))
            st,sp = a[i],i

    return OP

def cal(cont_list):
    if len(cont_list) == 0:
        return 0
    else:
        output = 0
        for cl in cont_list:
            st,end = cl[0],cl[1]
            output += sum_of_n(end-st+1)
        return output

def sum_of_n(n):
    return n*(n+1)//2

def main():
    N = int(input())
    a = list(map(int,input().split()))

    cont_list = cont(a,N)
    ans = cal(cont_list)

    print(ans)

if __name__ == "__main__":
    main()
