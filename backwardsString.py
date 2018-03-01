"""
#Practice

a = [1,2,3,4,5,6,7,8]
print(a[0:3])
print(a[0:8:2]) #print index 0 - 8, incrementing 2x index - gives odd numbers in this case
print(a[-1]) #prints number 8
print(a[:8]) #prints all indexes up to the 8th
print(a[::]) #prints all values from beginning to end of the array. Don't need to specify with ( len(a) )
print(a[::-1]) #prints all values of the array , incrementing by -1. Essentially prints array backwards

"""


#function (backwards_string) that takes an arguement
def backwards_string(word):
    # starts with an empty list called character
    character = []
    #for every variable (letter) in arguement (word)
    for letter in word:
        #add the variable (letter) to list (character)
        character.append(letter)
    #print the list (character) from beginning to end of the list, incrementing by -1
    print(character[::-1])

backwards_string("Brigittie")


#function called string_printer that takes arguement (word)
def string_printer(word):
    #starts off with an empty string called (build_word)
    build_word = ""
    #for every variable (letter) in arguement (word)
    for letter in word:
        #add variable (letter) and string (build_word), and assign the result to (build_word)
        build_word = letter + build_word
    #print the new value of build_word
    print(build_word)

string_printer("brigittie")


#https://wiki.python.org/moin/ForLoop






