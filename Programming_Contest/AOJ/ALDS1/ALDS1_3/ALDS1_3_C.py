from collections import deque

n = int(input())
DL = deque()
for i in range(n):
    com = input()
    if com == "deleteFirst":
        DL.popleft()
    elif com == "deleteLast":
        DL.pop()
    else:
        c,s = com.split()
        if c == "insert":
            DL.appendleft(s)
        elif c == "delete":
            try:
                DL.remove(s)
            except:
                pass
print(" ".join(list(DL)))
