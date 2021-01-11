import time
import msvcrt as ms
clue = 3


def main():
    try:
        inp = int(input("\nChoose Your Favourite number from 1 to 3: "))
    except ValueError:
        print("Oops, Alphabatic characters aren't accepted in this game\n Please Try Again\n")
        main()
    else:
        print(f"Wow {inp} is a great choice\n All the best")
        print("-" * 15)
        if inp == 1:
            first()
        elif inp == 2:
            second()
        elif inp not in [1, 2, 3]:
            print("\ninvalid Digit, Please Try Again\n")
            main()
        else:
            inp == 3
            third()


def count():
    count = 0
    count += 1
    print(f"The Point is {count}\n")


def wait():
    name = input("\nWhat's Your Name: ")

    def countdown(t):
        while t:
            mins, secs = divmod(t, 60)
            timer = '{:02d}:{:02d}'.format(mins, secs)
            print(f'Hold on {name}, The game begins in:', timer, end="\r")
            time.sleep(1)
            t -= 1

    countdown(int(3))


def right1():
    print("\nWoah, Your first guess is correct")
    count()


def right2():
    print("\nWoah Your Second Answer is Correct")
    count()


def wrong():
    print("\nWrong Answer")


def enter():
    e = str(input("\nEnter The First Missing letter or Type X for Clue: ")).upper()
    return e


def enter2():
    p = str(input("Enter the second Missing letter or Type X for Clue: ")).upper()
    return p


def missing_l():
    m = print("\n\nFind the Missing letter in")
    return m


def total_clue():
    global clue
    if clue == 0:
        print(f"Outta Clues yo, {clue} left\n Retry...\n")
        loop()
    else:
        print(f"The total clues left: {clue}\n")


def first():
    wait()
    missing_l()
    ar_ques()


def ar_clue():
    print("\nClue: \n An American Singer, Songwriter, Actress\n")
    global clue
    clue -= 1
    total_clue()
    ar_ques()


def ar_clue2():
    print("\nClue: \n Related to an American Sitcom VICTORIOUS\n")
    global clue
    clue -= 1
    total_clue()


def ar_ques():
    print("AR_ANA GRAN_E")
    x = enter()
    if x == "I":
        right1()

    elif x == "X":
        ar_clue()

    else:
        wrong()
        print('it was "I"\n')

    i = enter2()
    if i == "D":
        right2()

    elif i == "X":
        ar_clue2()

    else:
        wrong()
        print('It was "R"\n')


def second():
    wait()
    missing_l()
    br_ques()


def br_clue1():
    print('Clue: \n Famous Comicbook Character whose Alter Ego is "Batman"')
    global clue
    clue -= 1
    total_clue()
    br_ques()


def br_clue2():
    print('Clue: \n Related to the fictional city of DC Comics "Gotham"')
    global clue
    clue -= 1
    total_clue()


def br_ques():
    print("BR_CE WA_NE")
    y = enter()
    if y == "U":
        right1()

    elif y == "X":
        br_clue1()

    else:
        wrong()
        print('It was "U"\n')

    j = enter2()
    if j == "Y":
        right2()

    elif j == "X":
        br_clue2()

    else:
        wrong()
        print('It was "Y"\n')


def third():
    wait()
    missing_l()
    hr_ques()


def hr_clue():
    print('\nClue: \n He Played a fictional character "Han Solo" in Star Wars Franchise\n')
    global clue
    clue -= 1
    total_clue()
    hr_ques()


def hr_clue2():
    print("\nClue: \n He's a Hollywood Actor, Pilot, Environmental Activist\n")
    global clue
    clue -= 1
    total_clue()


def hr_ques():
    print("HARRI_ON F_RD")
    z = enter()
    if z == "S":
        right1()

    elif z == "X":
        hr_clue()

    else:
        wrong()
        print(f'It was "S"\n')

    k = enter2()
    if k == "O":
        right2()

    elif k == "X":
        hr_clue2()
    else:
        wrong()
        print('It was "O"\n')


def loop():
    while True:
        ex = input("Do you wanna play again? [Y/N]: ").upper()
        if ex == "Y":
            main()
        else:
            ex != "Y"
            print('\nPlease press "ENTER" to Confirm')
            ms.getch()
            print("Adios Amigo...\n")
            break


def all():
    main()
    loop()


all()

