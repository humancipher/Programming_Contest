def hash(a):
    return ord(a) - ord("a") + 1

def rev_hash(n):
    return chr(n + ord("a") - 1)

def solve(pw):
    if pw == "a" or pw == "z"*20:
        return "NO"
    else:
        PWL = list(pw)
        if len(set(PWL)) >= 2:
            flag = False
            for i in range(len(PWL)):
                for j in range(i+1,len(PWL)):
                    if PWL[i] != PWL[j]:
                        PWL[i],PWL[j] = PWL[j],PWL[i]
                        flag = True
                        break
                if flag:
                    break
            return "".join(PWL)
        else:
            if len(pw) >= 2:
                if pw[0] == "a":
                    PWL[-2] = "b"
                    return "".join(PWL[:len(PWL)-1])
                elif pw[0] == "z":
                    PWL[-1] = "y"
                    return "".join(PWL) + "a"
                else:
                    PWL[-2] = rev_hash(hash(PWL[-2])+1)
                    PWL[-1] = rev_hash(hash(PWL[-1])-1)
                    return "".join(PWL)
            else:
                PWL[-1] = rev_hash(hash(PWL[-1])-1)
                return "".join(PWL) + "a"                    

def main():
    pw = input()
    print(solve(pw))

if __name__ == "__main__":
    main()
