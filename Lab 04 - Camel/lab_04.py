import arcade
import random


miles_traveled = 0
thirst = 0
camel_tiredness = 0
native_distance = -20
canteen_drinks = 3

def main():
    print("Welcome to Camel!\nYou have stolen a camel to make your way across the great Mobi desert.\nThe Natives want their camel back and are chasing you down! Survive your\ndesert trek and out run the natives.")
    done=False
    while not done:
        print("A. Drink from your canteen.\nB. Ahead moderate speed.\nC. Ahead full speed.\nD. Stop for the night.\nE. Status check.\nQ. Quit.")
        user_choice = input("What is your choise? ")
        if user_choice == "q":
            Q = input ("Do you wish to quit? ")
            if Q == "y":
                done=True
                print("Thanks for Playing!")
            if Q == "n":
                done=False
                print("You continue your journey...")

        elif user_choice == "e":
            E = print("Status\nMiles Traveled",miles_traveled,"\nThirst",thirst,"\nCamel Tiredness",camel_tiredness,"\nNative Distance",native_distance,"\nCanteen Drinks",canteen_drinks,".")

        elif user_choice == "d":
            native_miles = random.randrange(7,14)
            D = print("The camel is happy but the natives move ",native_miles," miles closer.")

        elif user_choice == "c":
            miles_traveled_1 = random.randrange(10,20)
            C = print("You have traveled ",miles_traveled_1," miles.")

        elif user_choice == "b":
            miles_traveled_2 = random.randrange(5,12)
            B = print("You have traveled ",miles_traveled_2,"miles.")

        elif user_choice == "a":
            print("You have ",canteen_drinks," drinks left.")
main()