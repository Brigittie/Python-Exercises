"""
#original

def f(a):
    b = 0
    for c in a:
        if c > b:
            b = c
    return b


def g(d):
#print the string name of the function "F", _____, run function f with argument d
    print "{111}({222}) = {333}"  .111format(f.__name__,   222  d,  333   f(d))


g([1, 2, 3])
g([-1, 9, 5, 2])
g([7, 4, 3, 1])
g([1, -1])
g([3, 0, 3])
"""

def evaluate_highest_number_in_array(any_array):
    high_number = 0
    for index_in_array in any_array:
        if index_in_array > high_number:
            high_number = index_in_array
    return high_number


def what_is_highest_number_in_array(user_array):
    #print(the string name of "evaluate highest number in array + user array",
    #and print results from "evaluate highest number in array" with "user array" arguement in string format
    print("{}({})={}".format(evaluate_highest_number_in_array.__name__,user_array, evaluate_highest_number_in_array(user_array)))


what_is_highest_number_in_array([1, 2, 3])
what_is_highest_number_in_array([-1, 9, 5, 2])
what_is_highest_number_in_array([7, 4, 3, 1])
what_is_highest_number_in_array([1, -1])
what_is_highest_number_in_array([3, 0, 3])
