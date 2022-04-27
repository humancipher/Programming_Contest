N = int(input())
S = input()

def _rot(c,N):
    if 'A' <= c and c <= 'Z':
        c = chr((ord(c) - ord('A') + N) % 26 + ord('A'))
    if 'a' <= c and c <= 'z':
        c = chr((ord(c) - ord('a') + N) % 26 + ord('a'))
    return c

def rot(S,N):
    g = (_rot(c,N) for c in S)
    return ''.join(g)

print(rot(S,N))
