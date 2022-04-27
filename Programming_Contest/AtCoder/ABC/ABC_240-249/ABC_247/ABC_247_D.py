from collections import deque

DQ = deque()
Ans = []
q = int(input())
for _ in range(q):
    s = list(map(int,input().split()))
    if s[0] == 1:
        DQ.append((s[1],s[2]))
    else:
        cnt = s[1]
        ans = 0
        while cnt > 0:
            a,b = DQ.popleft()
            if b <= cnt:
                ans += a * b
                cnt -= b
            else:
                ans += a * cnt
                DQ.appendleft((a,b-cnt))
                cnt = 0
        Ans.append(ans)
for i in range(len(Ans)):
    print(Ans[i])