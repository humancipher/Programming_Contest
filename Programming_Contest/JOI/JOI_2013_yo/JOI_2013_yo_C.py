def judge(name,board):
    A,B = [],[]
    for i in range(len(board)):
        if board[i] == name[0]:
            A.append(i)
        if board[i] == name[1]:
            B.append(i)
    for a in A:
        for b in B:
            if a < b:
                d = b - a
                pt_b,pt_n = b + d,2
                while pt_b < len(board):
                    if board[pt_b] != name[pt_n]:
                        break
                    pt_b += d
                    pt_n += 1
                    if pt_n >= len(name):
                        return True
    return False

N = int(input())
name = input()
Board = [input() for _ in range(N)]

ans = 0
for i in range(N):
    if judge(name,Board[i]):
        ans += 1

print(ans)
