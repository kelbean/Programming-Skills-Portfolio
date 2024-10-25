"""

Exercise 02 - Simple Sums
By: Kelvin Bautista
CCL4

"""

# Variables

num1 = 8 # Storing the integer 8 in the num1 variable
num2 = 10 # Storing the integer 10 in the num2 variable
sum = (num1 + num2) # By using an addition operator, we can add num1 which is 8 and num2 which is 10.

# Printing the sum

print(f"The sum of {num1} and {num2} is {sum}.") # I used an f-string here to make it more readable.

# F-strings are used to format strings.
# By using them, it can be easier to add variables or expressions, making the command more readable.

"""

=== Extra ===

"""

# Added a few extra commands to get the user's input.
# Made use of a while loop here to keep asking for the user's input until they give a valid response.
# I added this to handle errors.

while True:
    try: # To initiate something that may cause an error.
        user_num1 = int(input("Let's try this again. Give me a number: ")) # User input
        break # To stop asking for the user's input once they give a valid response.

    # If the user decides to be rebellious and types anything other than an integer, it is handled here below:

    except ValueError:
        print("Please enter a numerical value!")

# Same case for the second number below:

while True:
    try:
        user_num2 = int(input("Alright, now give me another number: "))
        break

    except ValueError:
        print("Please enter a numerical value!")

# Adding both user inputs:

user_sum = user_num1 + user_num2

# Printing the sum of both user inputs:

print(f"Adding those both, we get {user_sum}! I'm pretty smart, huh?")

'''

Comments:
In this activity, I managed to learn about while loops to handle errors.

Of course, some users can be quite troubling and they tend to type anything other than
what the program is asking for. As a result, we must learn how to handle these errors.

Since users might type special characters or alphabets, I added a while True loop to keep repeating
the question in the 'try' block until the user has given a valid integer as a response.

If the user has given an invalid response, it will initiate the command in the 'except' block
and repeat the question again.

But if the user has given a valid response, it will 'break' the loop which will stop asking the question
repeatedly and move on to the next lines of code.

Overall, I learned more about error handling here which made the exercise really fun.

'''
