from math import sqrt

def manhatan(X):
    ans  = 0
    for x in X:
        ans += abs(x)
    return ans

def euclid(X):
    ans = 0
    for x in X:
        ans += x**2
    return sqrt(ans)

def tyebichef(X):
    ans = 0
    for x in X:
        ans = max(ans,abs(x))
    return ans

n = int(input())
X = list(map(int,input().split()))
print(manhatan(X))
print(euclid(X))
print(tyebichef(X))
