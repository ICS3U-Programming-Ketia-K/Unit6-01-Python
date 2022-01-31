#!/usr/bin/env python3

# Created by: Ketia Gaelle Kaze
# Created on: Jan. 27, 2022
# This program uses a for loop to generate
# 10 random numbers in a list and then
# calculate the average and display it.

import constants
import random


def main():
    # initialize sum and counter
    sum = 0
    loop_counter = 0

    # declare variable
    list_of_ints = []

    # display opening message to the user
    print("This program generates a list of 10 random "
          "numbers between 0 and 100 and then it calculates the average.")
    print("")

    # display random numbers and calculate average
    for loop_counter in range(constants.MAX_ARRAY_SIZE):
        list_of_ints.append(random.randint
                            (constants.MIN_NUM, constants.MAX_NUM))
        sum = sum + list_of_ints[loop_counter]
        print("{} added to the list at "
              "position {}" .format(list_of_ints[loop_counter], loop_counter))

    # determine if array is full and then calculate and display average

    for loop_counter in range(1):
        average = sum / constants.MAX_ARRAY_SIZE
        print("")
        print("The average is: {}" .format(str(average)))


if __name__ == "__main__":
    main()
