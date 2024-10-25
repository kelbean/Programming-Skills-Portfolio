"""

Exercise 03 - Biography
By: Kelvin Bautista
CCL4

"""

# Making my own biography here using a dictionary:

my_biography = {"Name": "Kelvin",
                "Hometown": "Bataan, Philippines",
                "Age": 18
                }

# To display my biography using a single print statement, I made use of \n which creates a new line.

print(f" \n===== My Biography =====\n \nName: {my_biography['Name']}\nHometown: {my_biography['Hometown']}\nAge: {my_biography['Age']}\n \n========================")

# Now, let's make a biography from the user's input.

# Getting the user's details and adding them into a dictionary is going to require a lot of lines
# For the sake of convenience and so that I can make my code more organized, I will be using a function:

def get_user_info(): # Added a function here to reuse it later on.
    
    user_name = input("Enter your name: ") # Asking for the user's name to input it into the user's dictionary.
    
    user_hometown = input("Enter your hometown: ") # Asking for the user's hometown to input it into the user's dictionary.

    while True: # Added a while loop here to keep asking until the user gives a valid age.
        try:
            user_age = int(input("Enter your age: ")) # Asking for the user's age to input it into the user's dictionary.

            if user_age <= 0: # If user typed negative or equal to 0, it will ask again.
                print("You haven't even been born yet. Please type a valid age.")
            

            elif user_age > 130: # If user has typed over 130, it will ask again as the given age is too bizarre.
                print("You know you won't be alive anymore by that age unless you're some sort of vampire!\nPlease be honest.")
            
            else: # Loop is broken if user has given a valid answer.
                break
            
        except ValueError: # If user has entered alphabetical letters or special characters, it will ask again.
            print("Please enter a valid age.")

# User dictionary is created based on the info stored in the variables:

    user_biography = { "Name": user_name,
                        "Hometown": user_hometown,
                        "Age": user_age
}
    
    return user_biography # Now, we're going to return the stored information back to the caller.

# Now, it's time to ask the user if they wanna make their own biography!

while True:
    ask_user_biography = input("Would you like to create your own biography? (Y/N) ")
    ask_user_biography = ask_user_biography.upper() # To avoid capitalization errors, this line will convert any response to uppercase.

    # If the user says Y, this will start the process of asking the user's details.

    if ask_user_biography == "Y":
        user_info = get_user_info() # Reusing the function I made from earlier by calling it.
        # With the user's details, it will print the created dictionary.
        print(f" \n===== Your Biography =====\n \nName: {user_info['Name']}\nHometown: {user_info['Hometown']}\nAge: {user_info['Age']}\n \n==========================")
        break # To stop asking once the user has given a valid response.
        
    # If the user says N, then the program says goodbye :(

    elif ask_user_biography == "N":
        print("Aww, okay then. Goodbye :(")
        break

    else: # If the user typed an invalid response, it will ask again.
        print("Please give a valid answer.")

'''

Comments:
This took a long time but that's only because I decided to learn about functions early.

If I didn't make use of them, then I would have to directly place all the code of
collecting the user's info under the if statement which would make it extremely hard to manage.

Functions are a great way to organize code. With their help, you can basically reuse
large lines of code in other sections of the program. It's super convenient!

Anyways, other than that, making the biography and asking for the user's input wasn't too hard.
It only took me a while to figure out the right indentations and layout of the loops and
if-else statements.

Overall, I'd say this exercise was challenging but fun at the same time.

'''