def backwards_sentence(sentence):
    word_list = sentence.split(" ") #splits my sentence into a list, using "space" as the delimiter
    list_of_strings = (word_list[::-1]) #returns my list of words from beginning to end of array, with -1 increment

    print(" ".join(list_of_strings))

"""
    strings_added_together = " "
    for list_of_strings in word_list:
        strings_added_together = list_of_strings + " "+ strings_added_together
    print(strings_added_together)
"""
backwards_sentence("It is sunny")



