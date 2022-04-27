N = int(input())
SL = set([input() for _ in range(N)])

Set = set([])
ans = "satisfiable"
for s in SL:
    if s[0] == "!":
        t = s[1:]
    else:
        t = s
    if t in Set:
        ans = t
        break
    else:
        Set.add(t)

print(ans)
