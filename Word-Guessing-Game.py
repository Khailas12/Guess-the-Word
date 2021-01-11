word = "Bruce"
guess = ""
command = ""

while guess != word:
    print("Identify the Missing Letter in 'Br_ce'")
    command = input("\nDo u wanna play [Y/N]: ").upper()
    if command == "Y":
        print("let's begin")
    elif command == "N":
        print("Alright Cool")
        break
    else:
        command != "Y" and "N" 
        o = input("\nOops, Invalid entry. Do u wanna continue [Y/N]: ").upper()
        if o == "Y":
            print("Woah, You made it clear, Let's go again")
        else:
            o == "N"
            print("Alright bye")
            break
            

    guess = input("\nEnter the letter: ").upper()
    if guess == "U":
        print("You Won")
        break
    else:
        guess != "U"
        print("\nTry Again")
           

