def function_f(arguement_a):
    #sets b to value 0
    stored_value = 0
    #for the parameter ___ in
    for the_number_in_array in arguement_a:
        if the_number_in_array > stored_value:
            stored_value = the_number_in_array
    return stored_value


def function_g(arguement_d):
    print("{}({})={}".format(function_f.__name__,arguement_d, function_f(arguement_d)))


function_g([1, 2, 3])
function_g([-1, 9, 5, 2])
function_g([7, 4, 3, 1])
function_g([1, -1])
function_g([3, 0, 3])
