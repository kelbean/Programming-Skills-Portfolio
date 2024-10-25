"""

Exercise 10 - Is it even?
By: Kelvin Bautista
CCL4

"""

# Here, I made a function with the parameter (x) to determine if the value is even or odd:

def even_or_odd(x):
    if x % 2 == 0: # If x divided by 2 has a remainder of 0, then x is an even number.
        return f"Fun fact: {x} is an even number!"

    else: # Anything else would be an odd number.
        return f"Fun fact: {x} is an odd number!"

# Now, I made the function where the program starts asking the user for a number.

def main():
    while True:
        try:
            user_input = int(input("Yo, give me a number: "))
            result = even_or_odd(user_input) # This calls the function with the user's input as an argument.
            print(result) # Whatever was stored in result, it will be printed here.
            break # This breaks the loop once a valid response is given.

        # If an invalid response is given, it asks again:

        except ValueError:
            print("Valid integer please!")

main() # Now, let's call the main function to start the program.

'''

Comments:
I'm not gonna lie. When I first saw the instructions for this exercise, I thought that
it was going to be a piece of cake. That was until I started doing it.

I got confused along the way because I never really understood the passing of arguments to
functions. Additionally, the structure of these functions kinda overwhelmed me. Maybe I
just needed sleep?

Anyways, it may have taken me a long time to understand them but thankfully, I managed
to pull through. Now, I see why this was the final exercise. It's simple but it'll only
work out for you if you truly understand functions. I definitely got humbled..

It was fun though!

'''
