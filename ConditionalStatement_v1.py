"""
if in is odd print weird
if n is even and within 2-5 print not weird
if n is even and within 6-20 print weird
if n is even and greater than 20 print not weird
"""

def is_weird_or_not (user_input):
    while user_input >= 1 and user_input <= 100:
        if (user_input%2)!= 0:
            print("{} is Weird".format(user_input))
            elif user_input >= 2 and user_input <= 5:
                print(("{} is Not Weird".format(user_input)))
            elif user_input >= 6 and user_input <= 20:
                print(("{} is Weird".format(user_input)))
            elif user_input > 20:
                print(("{} is Not Weird".format(user_input)))
        else:
            print("Does not compute")

is_weird_or_not(-3)
is_weird_or_not(3)
is_weird_or_not(4)
is_weird_or_not(4)
is_weird_or_not(18)
is_weird_or_not(22)
