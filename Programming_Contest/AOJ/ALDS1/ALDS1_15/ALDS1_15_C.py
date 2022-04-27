def act(st):
    st.sort(key = lambda x:x[0])
    OP = [st[0]]

    for i in range(1,len(st)):
        if OP[len(OP)-1][1] < st[i][0]:
            OP.append(st[i])
        elif OP[len(OP)-1][1] <= st[i][1]:
            pass
        else:
            OP.pop()
            OP.append(st[i])
    return len(OP)

def main():
    n = int(input())
    st = [tuple(map(int,input().split())) for _ in range(n)]

    ans = act(st)
    print(ans)

if __name__ == "__main__":
    main()
