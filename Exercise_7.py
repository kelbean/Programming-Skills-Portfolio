"""

Exercise 07 - Some Counting
By: Kelvin Bautista
CCL4

"""

import time # I imported the time module so I can delay code execution.

# Since I didn't want each loop to be activated all at once, I modified it in a sort of vending machine style.

# The user will pick a number based on the loop that they want to activate.

# If they choose 6, it exits the program.

loops_dictionary = {1 : "Loop that counts up from 0 to 50 in increments of 1.",
                    2 : "Loop that counts down from 50 to 0 in decrements of 1.",
                    3 : "Loop that counts up from 30 to 50 in increments of 1.",
                    4 : "Loop that counts down from 50 to 10 in decrements of 2.",
                    5 : "Loop that counts up from 100 to 200 in increments of 5.",
                    6 : "Exit the program."
}

print() # Just added a space here to make it look organized when it executes.

# I added a single print statement here to show the options that the user can choose. It's like a menu.

print(f"( 1 ): {loops_dictionary[1]}\n( 2 ): {loops_dictionary[2]}\n( 3 ): {loops_dictionary[3]}\n( 4 ): {loops_dictionary[4]}\n( 5 ): {loops_dictionary[5]}\n( 6 ): {loops_dictionary[6]}\n")

while True: # While loop to keep executing until given a valid response.

    try:
        choose_a_loop = int(input("Please choose a loop to activate! (1-6): "))

    # Loop that counts up from 0 to 50 in increments of 1:

        if choose_a_loop == 1: # If they chose 1, it activates this loop.
            print("Okay!\n \n==========\n ")
            for x in range(0,51,1):
                print(x)
                time.sleep(0.01) # Each element that is executed in the range will be delayed by 0.01 second.
            print(" \n==========\n ")
            break

    # Loop that counts down from 50 to 0 in decrements of 1:

        elif choose_a_loop == 2: # If they chose 2, it activates this loop.
            print("Okay!\n \n==========\n ")
            for x in range(50,-1,-1):
                print(x)
                time.sleep(0.01) # Each element that is executed in the range will be delayed by 0.01 second.
            print(" \n==========\n ")
            break


    # Loop that counts up from 30 to 50 in increments of 1:

        elif choose_a_loop == 3: # If they chose 3, it activates this loop.
            print("Okay!\n \n==========\n ")
            for x in range(30,51,1):
                print(x)
                time.sleep(0.01) # Each element that is executed in the range will be delayed by 0.01 second.
            print(" \n==========\n ")
            break

    # Loop that counts down from 50 to 10 in decrements of 2:

        elif choose_a_loop == 4: # If they chose 4, it activates this loop.
            print("Okay!\n \n==========\n ")
            for x in range(50,9,-2):
                print(x)
                time.sleep(0.01) # Each element that is executed in the range will be delayed by 0.01 second.
            print(" \n==========\n ")
            break

    # Loop that counts up from 100 to 200 in increments of 5:

        elif choose_a_loop == 5: # If they chose 5, it activates this loop.
            print("Okay!\n \n==========\n ")
            for x in range(100,201,5):
                print(x)
                time.sleep(0.01) # Each element that is executed in the range will be delayed by 0.01 second.
            print(" \n==========\n ")
            break

    # Exit the program.

        elif choose_a_loop == 6: # If the user chooses 6, it exits the program.
            print("Goodbye!")
            exit()

    # If the user decides to type anything else, the program asks again.

        else:
            print("Invalid number. Please choose between 1 - 6.")

    except ValueError:
        print("Invalid response. Please choose between 1 - 6.")

'''

Comments:
I didn't want to execute each loop all at once so I decided to let the user choose
what they want to activate. Based on how I built the structure of this program, it
kinda reminds me of a vending machine.

Additionally, I imported the time module just because I wanna delay some code execution
when the loop activates. It looks way cooler that way!

Overall, this exercise was really fun! It might be my favorite out of the 10.

'''