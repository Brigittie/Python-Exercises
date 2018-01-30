
#print("What's your first name?")
firstName = input("What's your first name?")

#print("What's your last name?")
lastName = input("What's your last name?")

#print("How old are you?")
age = input("How old are you?")

#print("What's your hometown?")
home = input("What's your hometown?")

#print("Hello! " + firstName +" " + lastName+ "! You are " + age + " years old and you are from "+ home)
print("Hello! {} {}! It's nice to meet you. You are {} years old and you're from {}.".format(firstName, lastName, age, home))

