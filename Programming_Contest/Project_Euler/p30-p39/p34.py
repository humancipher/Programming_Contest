def judge(fact,n):
    m,check_sum = str(n),0
    for i in range(len(m)):
        check_sum += fact[int(m[i])]
    if check_sum == n:
        return True
    else:
        return False

fact = [1,1]
for i in range(1,9):
    fact.append(fact[len(fact)-1]*(i+1))
N = fact[9]*7
#fact = [1, 1, 2, 6, 24, 120, 720, 5040, 40320, 362880]
#fact[i]:iの階乗
#各桁の階乗の和が元の数値と一致するとしたらその数値は9!*7未満
#9!*8が7桁なので8桁より大きい数値ではありえない
ans = 0
for i in range(3,N):
    if judge(fact,i):
        ans += i
print(ans)
