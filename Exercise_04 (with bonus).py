"""

Exercise 04 - Primitive Quiz
By: Kelvin Bautista
CCL4

"""

# Here, I made a dictionary to keep track of each country's capital as reference for the program:

primitive_quiz = {"France": "Paris",
                  "United Kingdom": "London",
                  "Germany": "Berlin",
                  "Italy": "Rome",
                  "Spain": "Madrid",
                  "Sweden": "Stockholm",
                  "Netherlands": "Amsterdam",
                  "Greece": "Athens",
                  "Denmark": "Copenhagen",
                  "Ukraine": "Kyiv"
                }

# I added a for loop here to iterate over each country and capital in the dictionary above.
# Adding this for loop was definitely a game changer!
# If I didn't use for loops and dictionaries, I would have to manually type out each question while checking each answer.

for country, capital in primitive_quiz.items(): # country, capital is basically key, value in the dictionary
# By using the items() method, I can work with the key-value pairs in the dictionary.

# I created a while True loop here to make it keep running until the user has given the right answer.

    while True:
        question = input(f"What is the capital of {country}? ") # {country} is the key in dictionary.
        question = question.lower() # Converting the user input to lowercase to match the right answer.

# Added an extra option here to give the user the ability to exit the program. Just in case they get bored. :P

        if question == "q":
            print("Oh, okay. Goodbye!")
            exit()

# Made an elif statement here. If they instead typed the right answer, it would say correct and break the loop.
# If their answer matches the value of the key, it moves on to the next key.

        elif question == capital.lower(): # To avoid problems in capitalization, the capital is converted to lowercase in order to match the user's input.
            print("Good job, that's correct! Moving on..")
            break

# If they type anything else other than the answer, it would say incorrect. They are also given the option to try again or quit.

        else:
            print("Yikes, that's incorrect. Try again or type 'q' to quit.")

# Once the quiz is finished, it will print this message.

print("Quiz completed! Well done, you have finished the quiz.")

'''

Comments:
This one was a little tougher to figure out. Of course, I didn't want to just
manually print out each question and use if-else statements to check if the answer
is right or not. That would require many lines of code!

So instead, I decided to research about for loops. At first, I wasn't too familiar
with them. However, when I learned that they can repeat actions for each item in a
sequence, an idea popped right into my head.

I decided to make a dictionary of countries pairing them up with their capital.
So by using for loops, it can iterate over each key-value pair in the dictionary
and repeat actions. Using them was definitely a big help.

'''
