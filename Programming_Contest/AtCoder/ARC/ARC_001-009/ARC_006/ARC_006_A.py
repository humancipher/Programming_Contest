def judge(E,B,L):
    cnt,bonus = 0,False
    for l in L:
        if l in E:
            cnt += 1
        elif l == B:
            bonus = True
    
    if cnt == 6:
        return 1
    elif cnt == 5 and bonus:
        return 2
    elif cnt == 5:
        return 3
    elif cnt == 4:
        return 4
    elif cnt == 3:
        return 5
    else:
        return 0

def main():
    E = set(list(map(int,input().split())))
    B = int(input())
    L = set(list(map(int,input().split())))

    print(judge(E,B,L))

if __name__ == "__main__":
    main()
