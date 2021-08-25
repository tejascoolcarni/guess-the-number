import random
print("Welcome to Jumanji!!!!")
input("(press enter)")
print("Lol kidding XD!\nHi! I'm Tejas. This is just a simple guessing game. I have thought of a number in my mind.\nAll you have to do is guess what the number is!\nYou have 10 attempts and after every guess,\nI will tell you if your guessed number is 'greater than' or 'less than'\nthan my number. Best of luck!")
continue_game= True
while(continue_game):
    input("(press enter)\n")
    while(True):
        k = input("Choose the difficulty level\nPress 'e' for Easy Mode\nPress 'm' for Medium Mode\nPress 'h'for Hard Mode\n").strip().lower()
        if k == "e":
            a = random.randint(0, 50)
            break
        elif k == "m":
            a = random.randint(0, 100)
            break
        elif k == "h":
            a = random.randint(0, 10002)
            break
        else:
            print("Wrong input! Try again.")

    x = 0
    while x <= 9:
        try:
            b = int(input("Guess the number\n"))
            if b > a:
                print("less than", b)
            elif b == a:
                print("Congratulations! You guessed it right.\nNumber of attempts taken:", x + 1)
                break
            else:
                print("greater than", b)
            print(9 - x, "attempts left.")
            x = x + 1
            if 10-x==0:
                print("Game Over.\nYou exhausted all attempts.")
                print("The number in my mind was", a)
        except:
            print("Enter a positive integer only")
    print("Would you like to try again?")

    while(True):
        c = input("Type y/n\n").strip().lower()
        if c == "y":
            break
        elif c == "n":
            print("Thank you for playing. :)")
            continue_game= False
            break
        else:
            print("Type 'y' for Yes/ Type 'n' for No ")









