#to select random output from list
# lst = ["snake", "water", "gun"]
# x = random.choice(lst)
# print(x)



import random
# a = 0 for snake
# a = 1 for water
# a = 2 for gun
comp_score = 0
your_score = 0
k = 1
while k <= 10:
    a = random.randint(0, 2)
    i = input("enter snake , water or gun\n")
    if a == 0 and i == "water":
        print("snake, you loose")
        comp_score += 1
    elif a == 0 and i == "gun":
        print("snake, you win")
        your_score += 1
    elif a == 0 and i == "snake":
        print("snake, Draw")
    elif a == 1 and i == "water":
        print("water, Draw")
    elif a == 1 and i == "gun":
        print("water, you loose")
        comp_score += 1
    elif a == 1 and i == "snake":
        print("water, you win")
        your_score += 1
    elif a == 2 and i == "water":
        print("gun, you win")
        your_score += 1
    elif a == 2 and i == "gun":
        print("gun, Draw")
    elif a == 2 and i == "snake":
        print("gun, you loose")
        comp_score += 1
    else:
        print("you have entered wrong input")
        continue
    k = k + 1
print("\nGAME OVER\n")
print("computer score is", comp_score)
print("your score is", your_score)
if comp_score > your_score:
    print("you have lost this game")
elif comp_score < your_score:
    print("you have won this game")
else:
    print("It's a tie")
