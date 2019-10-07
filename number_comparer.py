#!/usr/bin//env python3

# Created on: September 2019
# Created by: Paul Madut
# This is the a program used as a random number generator


def main():
    # This function does plays a game

    # Input
    user_number = int(input("Give a number: "))
    print(" ")
    # Process
    if user_number < 0:
        print("Your number is less than 0.")
    elif user_number == 0:
        print("Your number is 0")
    elif user_number > 0:
        print("Your number is bigger than 0")
    else:
        print("Bro ikd what to do")


if __name__ == "__main__":
    main()
