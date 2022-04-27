from bisect import bisect_left,bisect_right

S = input()

def b_search(Loop,key):
    #keyマス目から進んで入るループの場所とそこまでの距離
    if S[key] == "R":
        loop = Loop[bisect_left(Loop,key)]
        dist = loop - key
        return (loop,dist)
    else:
        loop = Loop[bisect_left(Loop,key)-1]
        dist = key - loop
        return (loop,dist)

Loop = []
for i in range(len(S)-1):
    if S[i] == "R" and S[i+1] == "L":
        Loop.append(i)

Ans = [0 for _ in range(len(S))]
for i in range(len(S)):
    loop,dist = b_search(Loop,i)[0],b_search(Loop,i)[1]
    if S[i] == "R":
        Ans[i+dist+(dist%2)] += 1
    else:
        Ans[i-dist+(dist%2)] += 1

ans = " ".join(map(str,Ans))
print(ans)
