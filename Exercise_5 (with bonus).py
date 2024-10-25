"""

Exercise 05 - Days of the Month
By: Kelvin Bautista
CCL4

"""

# Created a dictionary here assigning keys as the month number and the values as the number of days in that month.

days_of_the_month = { 1 : 31, # January
                     2 : 28, # February - has 29 days if leap year
                     3 : 31, # March
                     4 : 30, # April
                     5 : 31, # May
                     6 : 30, # June
                     7 : 31, # July
                     8 : 31, # August
                     9 : 30, # September
                     10 : 31, # October
                     11 : 30, # November
                     12 : 31 # December
}

# Made a separate dictionary to assign the month names to the month numbers. This is all for the last print statement.

month_names = { 1 : "January",
                2 : "February",
                3 : "March",
                4 : "April",
                5 : "May",
                6 : "June",
                7 : "July",
                8 : "August",
                9 : "September",
                10 : "October",
                11 : "November",
                12 : "December"
}

# Added a while loop here to keep asking until given a valid response.

while True:
    try:
        month_input = int(input("Enter a month number (1/12): "))

        if month_input < 1 or month_input > 12: # If the given month number is less than 1 or greater than 12, it asks again.
            print("Invalid month number. Please try again.")
        
        else:
            break # Loop is broken once given a valid response.

    except ValueError: # If response is anything other than numbers, it asks again.
        print("Invalid response. Please type a month number.")

# Leap year adjustment

if month_input == 2: # If the given month number is 2 (February), it initiates the commands below.
    while True:
        leap_year_question = input("Is it a leap year? (Y/N) ")
        leap_year_question = leap_year_question.casefold() # To avoid capitalization errors.

        if leap_year_question == "y": # If it is a leap year, it will adjust to 29 days.
            print("February has 29 days in a leap year.")
            break # Loop is broken once valid response is given.

        elif leap_year_question == "n": # If it is NOT a leap year, it will stick to 28 days.
            print(f"February has {days_of_the_month[2]} days in a common year.")
            break

        else: # If the user does not type Y/N, it asks again.
            print("Please type a valid answer.") 

else: # If the given month number ranges from 1 - 12 but is not 2, it will give the amount of days in that month.
    print(f"The month {month_names[month_input]} has {days_of_the_month[month_input]} days.")

'''

Comments:
Since I already learned about dictionaries and loops, this exercise wasn't too hard.
I just had to deal with a lot of error handling which wasn't too bad. I did have to
make two separate dictionaries so that the given month number matches what the month
name is. This is so that I could make a clear print statement at the end.

Other than that, the leap year adjustment command was mainly done with if-else statements.

'''