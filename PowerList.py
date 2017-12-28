"""
Exercises:

testList= [12, 24, 48, 36, 72]

print (testList)

#index starts at 0
print (testList[0])

#starts at beginning of list, wraps backwards 2 values
print (testList[-2])

#slices list and returns new one starting from value input
print (testList[2:])

#smoosh lists together!
print(testList + [1,2,3,4])

#changing the content of a list is easy!
testList[2]=69
print (testList)

#appending a string to my list
testList.append("some value")

#appending an equasion to my list
testList.append(3*2)

print(testList)

#what's the length of my list?
print (len(testList))

letterList = ["a","b","c","d","e","f","g"]

print (letterList)

#I can replace a range of values in my list
letterList[2:5] = ["C", "D", "E", "F"]
print (letterList)

#I can remove elements of my list
letterList[0:1] = []
print (letterList)

#I can remove everything from my list
letterList = []
print (letterList)

#make a list, containing other lists
letters = ["a","b","c"]
numbers = [1,2,3]

"""

"""
Problem:
create a list with all the square powers for the numbers between 1 and 10
not just printing them one by one, store them and then print all of them at once

"""

powerList = []
print (powerList)

#print (*range(1,11))

for i in range(1,11):
    i = i**10
    #print (i)
    powerList.append(i)
else:
    print ("Finito!")

print (powerList)




