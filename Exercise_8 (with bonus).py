"""

Exercise 08 - Simple Search
By: Kelvin Bautista
CCL4

"""

# Here, I made a list with all the names included.

name_list = ["Jake", "Zac", "Ian", "Ron", "Sam", "Dave"]

# Next, I made a function for the searching part. This is so that I can reuse it later:

def ask_question():
    name_search = input("Enter a name to search for: ") # User enters a name to search.
    name_search = name_search.capitalize() # To avoid capitalization errors, the user's input will be capitalized.

    if name_search in name_list: # If the given name is in the list, it'll print below:
        print(f"{name_search} found in list.")
        
    else: # If the given name is NOT in the list, it'll print below:
        print(f"{name_search} not found in list.")

question = ask_question() # Calling the function.

# I added a few extra commands below to find out if the user wants to search again.

while True:
    ask_again = input("Would you like to search for a name again? (Y/N): ")
    ask_again = ask_again.upper()

    # If user types Y then they can search for a name again.

    if ask_again == "Y":
        question = ask_question() # It calls the search function if the user wants to try again.

    # If user types N then womp womp, goodbye!

    elif ask_again == "N":
        print("Alright, goodbye!")
        break # This breaks the loop of asking again.

    # If user types anything else, it asks again.

    else:
        print("Please give a valid response.")
    
'''

Comments:
This exercise was also pretty fun. After a few exercises, I finally decided
to make use of functions again. They definitely helped in this case because
I wanted to reuse the ask_question command if the user wants to search for a
name again.

'''