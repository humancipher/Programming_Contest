from collections import Counter

n = int(input())
v = list(map(int,input().split()))

v_even,v_odd = [],[]
for i in range(n):
    if i % 2 == 0:
        v_even.append(v[i])
    else:
        v_odd.append(v[i])

c_even = Counter(v_even)
c_odd = Counter(v_odd)

if len(set(v)) == 1:
    ans = n // 2
elif len(set(v_even)) == 1:
    if c_even.most_common()[0][0] == c_odd.most_common()[0][0]:
        ans = (n // 2) - c_odd.most_common()[1][1]
    else:
        ans = (n // 2) - c_odd.most_common()[0][1]
elif len(set(v_odd)) == 1:
    if c_odd.most_common()[0][0] == c_even.most_common()[0][0]:
        ans = (n // 2) - c_even.most_common()[1][1]
    else:
        ans = (n // 2) - c_even.most_common()[0][1]
else:
    if c_odd.most_common()[0][0] != c_even.most_common()[0][0]:
        ans = n - c_even.most_common()[0][1] - c_odd.most_common()[0][1]
    else:
        ans = n - c_even.most_common()[0][1] \
              - max(c_even.most_common()[1][1],c_odd.most_common()[1][1])

print(ans)
