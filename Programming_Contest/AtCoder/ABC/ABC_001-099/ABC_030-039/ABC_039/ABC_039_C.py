def sound(S):
    loop = "WBWBWWBWBWBW"
    sound_list = ["Do","Si","La#","La","So#","So","Fa#","Fa","Mi","Re#","Re","Do#"]
    S = 2*S

    pt = S.find(loop)

    return sound_list[pt]

def main():
    S = input()

    print(sound(S[:12]))

if __name__ == "__main__":
    main()
