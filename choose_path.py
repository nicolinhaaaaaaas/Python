name = input("Type your name: ")
print("Welcome", name, "to this adventure!")

answer = input(
    "You are on a dirt road, it has come to an end and you can go left or right. Which way you choose? ")

if answer == "left":
    answer = input("You come to a river, you can walk around it or swim across. Type 'Walk' to walk around it, or 'swim' to swim across ")

    if answer == "swim":
        print("You swam across and were eaten by an alligator")
    elif answer == "walk":
        print("You walked for many miles, ran out of water and you lost the game")
    else:
        print("Not a valid option. You lose")

elif answer == "right":
    answer = input("You havee come to a bridge, it looks broken. Do you want to cross it or head back? (cross/back) ")

    if answer == "back":
        print("You go back and lose")

    elif answer == "cross":
        answer = input("You cross the bridge and meet a stranger. Do you want to talk to them? (yes/no) ")

        if answer == "yes":
            print("You talk to the stranger and they give you a hug. YOU WIN")
        elif answer == "no":
            print("You ignore the stranger and they kill you from the back. YOU LOSE")
        else:
            print("Not a valid option. You lose.")

    else:
        print("Not a valid option. You lose")

else:
    print("Not a valid option. You lose.")
