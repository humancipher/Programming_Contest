N = int(input())

def ans(n):
    if n % 2 != 0:
        return 0
    else:
        index,count = 1,0
        while 2 * 5**index <= n:
            count += n // (2 * 5**index)
            index += 1
    return count

print(ans(N))
