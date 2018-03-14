"""
Directions:
Given an integer n, print its first 10 multiples.
Each multiple n x i (where i <= i <= 10) should be printed
on a new line in the form: n x i = result.

Input:
single integer, n

Constraints:
2<= n <= 20

Output:
Print 10 lines of output; each line i  ((where i <= i <= 10) contains
the result of n x i in the form of
n x i = result
-------------------
scratchwork:
        #string_equation = str(user_input * multiples)
        #result = str(result)
        #multiplication_table_output = string_equation + "=" + result
        #print(multiplication_table_output)

"""

def multiplication_table(user_input):
    if 2<= user_input <= 20:
        user_input_string = str(user_input)
        for multiple in range(1,11):
            result = user_input * multiple
            result_string = str(result)
            multiple_string = str(multiple)
            print("{}*{}={}".format(user_input_string,multiple_string,result_string))

multiplication_table(3)




