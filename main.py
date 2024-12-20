print("Welcome to Treasure Island. \nYour mission is to find the treasure.")
first_choice = input('You are on the crossroad. Where do you want to go? \n      Type "left" or "right"\n').lower()
if first_choice == "right":
    print("You've been killed by wolves. \n      Game over.")
elif first_choice == "left":
    print("You've come to the lake. There is an island in the middle of the lake.")
    second_choice = input('   Type "wait" to wait for the boat, or "swim" to swim across. \n')
    if second_choice == "swim":
        print("You've been killed by sharks.  \n      Game over.")
    elif second_choice == "wait":
        print("You've arrived on island unharmed. There is a house with three doors. \nOne red, one yellow and one blue.")
        third_choice = input("Which door do you choose? \n")
        if third_choice == "red":
            print("Killer with an axe kills you. \n      Game over.")
        elif third_choice == "blue":
            print("Dragon emerges from the dark and kills you.  \n      Game over.")
        elif third_choice == "yellow":
            print("You have found the treasure. \n      You won.")
        else:
            print("You've entered wrong message. \n      Game over.")
    else:
        print("You've entered wrong message. \n      Game over.")
else:
    print("You've entered wrong message. \n      Game over.")


