#********************************************************************************************************
# TYPING, TYPE CASTING, & TYPE ERRORS
#********************************************************************************************************
print("\n*****************************************")
print("TYPING, TYPE CASTING, & TYPE ERRORS")
print("*****************************************\n")

# Python is DYNAMICALLY typed so variable types don't need to be explicitly declared. 
# The types are implicitly determined by the value assigned to the variable.
# Types are determined at runtime. 
# Type errors are detected when a program runs, not when it is compiled.

myName = 'Dakota' 
myMiddleName = "Natasha" 
myAgeInt = 29 
myHeight = 5.25
myWeight = 160.553553553553553553 
isStudent = False
myTuple = (1, 2, 3, 4, 5)
myRange = range(1, 10)
mySet = {7,5, 8, 6, 9}
myList = [1, 2, 3, 4, 5]
myDict = {'name': 'Dakota', 'age': 29, 'height': 5.25, 'weight': 160.553553553553553553, 'isStudent': False}

# Type Casting
myAgeString = str(myAgeInt)
myAgeFloat = float(myAgeInt)


# Notes: Type casting is the process of converting a variable from one data type to another. 
# Type casting can be done using built-in functions like str(), int(), float(), bool(), etc.

# Concatenating variables with strings and type casting the integer variable to a string variable.
print('My name is ' + myName + ' and I am ' + myAgeString + ' years old.')
# Note: type casting str(myAgeInt) is necessary to concatenate the integer variable with the string.

# Type Getting
print (type(myName))
print (type(myAgeInt))
print (type(myHeight))
print (type(isStudent))
print (type(mySet))
print (type(myList))
print (type(myDict))
print (type(myTuple))
print (type(myRange))

print (isinstance(myName, str))
print (isinstance(myAgeInt, int))



# Python is also STRONGLY typed, meaning that it does not allow implicit type conversion.
# For example, if you try to concatenate a string and an integer without type casting, a TypeError will be raised.

# Type Errors 
# (uncomment the following lines one at a time to see the TypeErrors)

# The following will NOT raise a TypeError because we are concatenating two string variables.
print(myName + myMiddleName)  

# The following will raise a TypeError because we are trying to subtract a string from an integer.
#print(myName - myAgeInt)

# The following will raise a TypeError because we are trying to concatenate a string and an integer without type casting.
#print(myName + myAgeInt)

# The following will not raise a TypeError because we converted the integer to a string before concatenating. 
print(myName + str(myAgeInt))

# The following will NOT raise a TypeError because we are multiplying a string by an integer. 
print(myName *3) 

# The following will raise a TypeError because we are trying to multiply a string by another string.
#print(myName * myMiddleName)

# The following will raise a TypeError because we are trying to multiply a string by a float.
#print(myName * 3.5)

# The following will raise a type error because range only accepts integer arguments, not float arguments.
#for i in range(myHeight):
    #print(i)

# The following will NOT raise a TypeError because we are type casting the float variable to an integer variable.
for i in range(int(myHeight)):
    print(i)
