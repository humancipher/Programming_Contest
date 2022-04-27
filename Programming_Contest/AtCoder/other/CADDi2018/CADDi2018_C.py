from math import sqrt

def fact(n):
    insu = []
    for i in range(2,int(sqrt(n))+1):
        if n % i == 0:
            while n % i == 0:
                n //= i
                insu.append(i)
        if n == 1:
            break
    if n > 1:
        insu.append(n)
    return insu

def main():
    N,P = map(int,input().split())
    insu = fact(P)
    insu_set,insu_list,pt = set(),[],0
    for i in range(len(insu)):
        if insu[i] not in insu_set:
            insu_set.add(insu[i])
            insu_list.append([insu[i],1])
            pt += 1
        else:
            insu_list[pt-1][1] += 1
    for i in range(len(insu_list)):
        insu_list[i][1] //= N

    ans = 1
    for a,b in insu_list:
        ans *= a**b
    print(ans)

if __name__ =="__main__":
    main()
