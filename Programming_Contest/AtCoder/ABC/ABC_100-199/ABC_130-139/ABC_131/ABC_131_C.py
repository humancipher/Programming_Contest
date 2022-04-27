from fractions import gcd

a,b,c,d = map(int,input().split())
a -= 1
def div(m,n):
	return m // n

ans_a = a - div(a,c) - div(a,d) + div(a,c*d//gcd(c,d))
ans_b = b - div(b,c) - div(b,d) + div(b,c*d//gcd(c,d))

print(ans_b - ans_a)
