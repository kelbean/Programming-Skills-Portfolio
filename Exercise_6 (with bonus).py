"""

Exercise 06 - Brute Force Attack
By: Kelvin Bautista
CCL4

"""

# Variables

correct_password = "12345"
password_attempts = 5

# I added a while loop here to keep asking for the user's name if given an invalid one. Just an extra.

while True:
    ask_username = input("Enter your username: ")
    avoid_special_characters = ask_username.isalnum() # This string method returns True if the username only consists of alphanumeric characters.
    
    if avoid_special_characters == False: # If the string method returns False, it tells the user to try again.
        print("Usernames cannot contain spaces or special characters. Try again.")
    
    else:
        break # Loop is broken once a valid username is given.

# I added a while loop here to ask for the user's password 5 times if given the wrong one.

while True:
    ask_password = input("Enter your password: ")

    if ask_password == correct_password: # If the user's input matches the correct password, access is granted.
        print(f"Access granted. Welcome back, {ask_username}!")
        break
    
    else:
        password_attempts -= 1 # If user types anything other than the password, attempts are subtracted by 1.
        print(f"Incorrect password. You have {password_attempts} attempts left.")

        if password_attempts == 0: # If number of attempts reaches zero, it alerts authorities and exits the program.
            print("You have no more attempts left. Authorities have been alerted.")
            exit()

'''

Comments:
This was a fun exercise. For a while, I've always been curious about the coding
for log-in screens. I know there are way more advanced password programs out there
but making a simple one for this exercise actually proved to be pretty easy.

Adding the username part at the beginning was only for extra. I wanted it so that
when the user puts in the right password, they're greeted with their username.

'''