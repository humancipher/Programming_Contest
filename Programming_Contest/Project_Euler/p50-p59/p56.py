def digit_sum(n):
    n = str(n)
    output = 0
    for i in range(len(n)):
        output += int(n[i])
    return output

def main():
    ans = 0
    for a in range(1,100):
        for b in range(1,100):
            if ans < digit_sum(pow(a,b)):
                ans = digit_sum(pow(a,b))
                a_maxi,b_maxi = a,b

    print(a_maxi,b_maxi)
    print(ans)

if __name__ == "__main__":
    main()
