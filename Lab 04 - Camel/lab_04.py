import arcade
import random

def main():
    miles_traveled = 0
    thirst = 0
    camel_tiredness = 0
    native_distance = -20
    canteen_drinks = 3
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
            native_distance += native_miles
            camel_tiredness = 0
            D = print("The camel is happy but the natives move ",native_miles," miles closer.")

        elif user_choice == "c":
            miles_traveled_1 = random.randrange(10,20)
            miles_traveled += miles_traveled_1
            thirst += 1
            camel_tiredness += random.randrange(1,3)
            native_distance += random.randrange(5,12)
            native_distance -= miles_traveled_1
            C = print("You have traveled ",miles_traveled_1," miles.")

        elif user_choice == "b":
            miles_traveled_2 = random.randrange(5,12)
            miles_traveled += miles_traveled_2
            thirst += 1
            camel_tiredness += 1
            native_distance += random.randrange(7,14)
            native_distance -= miles_traveled_2
            B = print("You have traveled ",miles_traveled_2,"miles.")

        elif user_choice == "a":
            canteen_drinks -= 1
            thirst = 0
            if canteen_drinks == -1:
                print("You are out of Canteen Drinks!")
            else:
                print("You have ", canteen_drinks, " drinks left.")
        if thirst > 4:
            print("You are thirsty!")
        if thirst > 6:
            done=True
            print("You died of Thirst!\n Game Over!")
        if camel_tiredness > 5:
            print("Your camel is tired!")
        if camel_tiredness > 8:
            done=True
            print("Your camel died!\n Game Over!")
        if native_distance >= 0:
            done=True
            print("The Natives have caught you!\n Game Over!")
        else:
            print("The Natives are getting close!")
        if miles_traveled >= 200:
            done=True
            print("You have escaped the Natives!")
        if random.randrange(20) == 0:
            canteen_drinks += 3
            thirst = 0
            camel_tiredness = 0
            print("You have found an Oasis!")
main()