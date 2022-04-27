S = input()
Ans = set()
for i in range(2**len(S)):
    left,right = 0,len(S)-1
    tmp_s = ""
    for j in range(len(S)):
        if 2**j & i:
            tmp_s += S[left]
            left += 1
        else:
            tmp_s += S[right]
            right -= 1
    Ans.add(tmp_s)
print(len(Ans))
