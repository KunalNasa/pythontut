x = 1
while (x<=5):
    guess_number = (int(input("guess the number\n")))
    if guess_number<20:
        print("guess bigger number")
    elif guess_number>20:
        print("guess smaller number")
    else:
        print("you have won this game")
        print(x, "number of guesses you took")
        break
    print(5-x,"guesses left")
    x = x + 1

if(x>5):
    print("GAME OVER")
