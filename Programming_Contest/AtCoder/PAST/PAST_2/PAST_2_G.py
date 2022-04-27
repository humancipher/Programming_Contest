from collections import deque

def operate(Q,N):
    S = deque()
    for i in range(N):
        if Q[i][0] == "1":
            c,x = Q[i][1],int(Q[i][2])
            S.append([c,x])
        else:
            d = int(Q[i][1])
            S_del,S_del_num = set(),{}
            while d > 0 and len(S) > 0:
                s = S.popleft()
                c,x = s[0],s[1]
                if x > d:
                    if c not in S_del:
                        S_del.add(c)
                        S_del_num[c] = d
                    else:
                        S_del_num[c] += d
                    x -= d
                    d = 0
                    S.appendleft([c,x])
                else:
                    if c not in S_del:
                        S_del.add(c)
                        S_del_num[c] = x
                    else:
                        S_del_num[c] += x
                    d -= x
            output = 0
            for c in S_del:
                output += S_del_num[c]**2
            print(output)

def main():
    N = int(input())
    Q = [list(input().split()) for _ in range(N)]

    operate(Q,N)

if __name__ == "__main__":
    main()
